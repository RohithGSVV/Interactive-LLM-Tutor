#!/usr/bin/env python3
TITLE = r"""
   ____ _                               ____  ____     ____ _ _            _   
  / ___| |__  _ __ ___  _ __ ___   __ _|  _ \| __ )   / ___| (_) ___ _ __ | |_ 
 | |   | '_ \| '__/ _ \| '_ ` _ \ / _` | | | |  _ \  | |   | | |/ _ \ '_ \| __|
 | |___| | | | | | (_) | | | | | | (_| | |_| | |_) | | |___| | |  __/ | | | |_ 
  \____|_| |_|_|  \___/|_| |_| |_|\__,_|____/|____/   \____|_|_|\___|_| |_|\__|
                                                                               
"""
from typing import List, Dict, Any
import chromadb
from chromadb.utils import embedding_functions
from chromadb.config import Settings
import argparse
import glob
import pandas as pd

CHROMADB_HOST = '10.230.100.212'
CHROMADB_PORT = 17026
CHROMADB_TOKEN = '44209e7e-9011-11ef-95b7-333cc912309b'
# # http://10.230.100.212:17026
# # Create a function to test persistent chromadb
# def test_chromadb_persistent_connection():
#     import chromadb
#     # from chromadb.config import Settings

#     # Create a chromadb client with the provided host, port, and token
#     client = chromadb.HttpClient(host=CHROMADB_HOST, port=CHROMADB_PORT)
    
#     # test the client to store a collection
#     # client.create_collection(name="my_collection")
#     collection = client.create_collection(name="my_collection")
#     collection.add(
#         ids=["id1", "id2"],
#         metadatas=[{"source": "test"}, {"source": "test"}],
#         documents=["test1", "test2"],
#     )
    

#     # Test the client by retrieving a collection
#     collection = client.get_collection(name="my_collection")
#     print(collection.query(query_texts=["test"], n_results=1))


# if __name__ == "__main__":
#     test_chromadb_persistent_connection()


class ChromaClient():
    def __init__(self, host, port, ssl=False, auth_token=None):
        self.host = host
        self.port = port
        self.ssl = ssl
        self.auth_token = auth_token
        self.client = None
        self.embedding_function = \
                embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        self.connect()

    # def __del__(self):
    #     if self.client is not None:
    #         self.client.reset()

    # def __exit__(self, exc_type, exc_value, traceback):
    #     if self.client is not None:
    #         self.client.reset()


    def connect(self):
        protocol = "https" if self.ssl else "http"
        url = f"{protocol}://{self.host}:{self.port}"

        try:
            self.client = chromadb.HttpClient(host=self.host, port=self.port, ssl=self.ssl)
            print(f"Successfully connected to ChromaDB at {url}")
        except Exception as e:
            print(f"Error connecting to ChromaDB at {url}: {str(e)}")


    def create_collection(self, name, embedding_function=None):
        if self.client is None:
            self.connect()
            if self.client is None:
                return None
        else:
            try:
                collection = self.client.create_collection(name=name, embedding_function=embedding_function)
                print(f"Successfully created collection '{name}'")
                return collection
            except Exception as e:
                print(f"Error creating collection: {str(e)}")
                return None
            

    def list_collections(self):
        if self.client is None:
            self.connect()
            if self.client is None:
                return None
        else:
            try:
                collections = self.client.list_collections()
                tab = pd.DataFrame.from_records([
                    collection.configuration_json for collection in collections
                ])
                # for collection in collections:
                #     print(collection.configuration_json)
                print(tab.to_markdown(index=None))
                return collections
            except Exception as e:
                print(f"Error listing collections: {str(e)}")
                return None
            

    def upload_documents(self, collection_name: str, 
                        documents: List[str], metadatas: List[Dict[str, Any]], 
                        ids: List[str]) -> Dict:
        
        if self.client is None:
            self.connect()
            if self.client is None:
                return None

        # Create an embedding function
        # embedding_function = embedding_functions.DefaultEmbeddingFunction()
        
        # Get or create the collection with the embedding function
        try:
            collection = self.client.get_or_create_collection(
                name=collection_name,
                embedding_function=self.embedding_function
            )
            print(f"Successfully got or created collection '{collection_name}' with embedding function")
        except Exception as e:
            print(f"Error getting or creating collection: {str(e)}")
            return False

        # Validate input data
        if len(documents) != len(metadatas) or len(documents) != len(ids):
            print("Error: documents, metadatas, and ids must have the same length")
            return False

        # Add documents to the collection
        try:
            # Generate embeddings for the documents
            embeddings = self.embedding_function(documents)
            print(f"Successfully generated embeddings for documents: {len(embeddings)}")

            collection.add(
                documents=documents,
                metadatas=metadatas,
                ids=ids,
                embeddings=embeddings
            )
            print(f"Successfully uploaded {len(documents)} documents to collection '{collection_name}'")
            return True
        except Exception as e:
            print(f"Error adding documents to collection: {str(e)}")
            return False

        


    def retrieve_top_matches(self, collection_name: str, query: str, n_results: int = 10) -> List[Dict]:
        # Ensure the client is connected
        if self.client is None:
            self.connect()
            if self.client is None:
                return []

        try:
            # Get the collection and query it
            collection = self.client.get_collection(name=collection_name, embedding_function=self.embedding_function)
            results = collection.query(
                query_texts=[query],
                n_results=n_results,
                include=["documents", "metadatas", "distances"]
            )

            # Format the results
            formatted_results = [
                {
                    'id': results['ids'][0][i],
                    'document': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'distance': results['distances'][0][i]
                }
                for i in range(len(results['ids'][0]))
            ]
            print(f"Successfully retrieved {len(formatted_results)} matches for query: '{query}'")
            return formatted_results

        except Exception as e:
            print(f"Error querying collection: {str(e)}")
            return []



def exec_list_collections(args):
    client = ChromaClient(
        host=args.host,
        port=args.port,
        ssl=args.ssl,
        auth_token=args.auth_token
    )
    results = client.list_collections()
    return results
    

def exec_upload_documents(args):
    client = ChromaClient(
        host=args.host,
        port=args.port,
        ssl=args.ssl,
        auth_token=args.auth_token
    )
    # Create an embedding function
    embedding_function = embedding_functions.DefaultEmbeddingFunction()

    # Get or create the collection with the embedding function
    collection = client.get_or_create_collection(
        name=args.collection,
        embedding_function=embedding_function
    )

    # Upload documents to the collection
    upload_success = client.upload_documents(
        collection_name=args.collection,
        documents=args.documents,
        metadatas=args.metadatas,
        ids=args.ids
    )
    if args.documents and args.metadatas and args.ids:
        upload_success = client.upload_documents(
            host=args.host,
            port=args.port,
            collection_name=args.collection,
            documents=args.documents,
            metadatas=args.metadatas,
            ids=args.ids,
            ssl=args.ssl,
            auth_token=args.auth_token
        )
        if upload_success:
            print("Documents uploaded successfully.")
        else:
            print("Failed to upload documents.")
    else:
        print("Please provide documents, metadatas, and ids.")
    return {}

def exec_retrieve_top_matches(args):
    client = ChromaClient(
        host=args.host,
        port=args.port,
        ssl=args.ssl,
        auth_token=args.auth_token
    )
    results = client.retrieve_top_matches(
        collection_name=args.collection,
        query=args.query,
        n_results=args.n_results,
    )
    print(results)



def help(args):
    print("ChromaDB Client")
    print("""

Commands:
    list: List all collections in the database
    upload: Upload documents to a collection
    retrieve: Retrieve top matching documents from a collection

Example usage:
    ./chromedb.py list
    ./chromedb.py upload --collection my_collection --documents "doc1" "doc2" --metadatas '{"source": "doc1"}' '{"source": "doc2"}' --ids "id1" "id2"
    ./chromedb.py retrieve --collection my_collection --query "search query" --n_results 5

""")
    parser.print_help()
    return {}


# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ChromaDB Client")
    parser.add_argument("COMMAND", type=str, help="Command to execute")
    parser.add_argument("--host", type=str, default=CHROMADB_HOST, help="ChromaDB host")
    parser.add_argument("--port", type=int, default=CHROMADB_PORT, help="ChromaDB port")
    parser.add_argument("--ssl", action="store_true", help="Use SSL for connection")
    parser.add_argument("--auth_token", type=str, default=CHROMADB_TOKEN, help="Authentication token (if required)")
    parser.add_argument("--collection", type=str, required=False, help="Collection name")
    parser.add_argument("--query", type=str, help="Query string")
    parser.add_argument("--n_results", type=int, default=10, help="Number of results to retrieve")
    parser.add_argument("--documents", type=str, nargs="+", help="Documents to upload")
    parser.add_argument("--metadatas", type=str, nargs="+", help="Metadatas for documents")
    parser.add_argument("--ids", type=str, nargs="+", help="IDs for documents")

    args = parser.parse_args()

    results = {
        "list": exec_list_collections,
        "upload": exec_upload_documents,
        "retrieve": exec_retrieve_top_matches
    }.get(args.COMMAND, help)(args)

    print(results)
    
