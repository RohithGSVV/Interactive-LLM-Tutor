import argparse
import os
import re
import json
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import PyPDFLoader # deprecated
from langchain_community.document_loaders import PyPDFLoader

def remove_headers_footers(text):
    text = re.sub(r'(CHAPTER\s\d+|Page\s\d+|Copyright.*\d{4})', '', text)
    text = re.sub(r'(?i)for instructor use only', '', text)
    return text

def remove_special_characters(text):
    text = re.sub(r'[^\w\s.,;]', '', text)
    return text

def remove_mcq_options(text):
    mcq_pattern = r'(?mi)^[a-d]\.\s+.*$'
    text = re.sub(mcq_pattern, '', text)
    return text

def remove_numbering(text):
    text = re.sub(r'^\d+\.\s+', '', text)
    return text

def replace_equations(text):
    equation_pattern = r'(\d+(\.\d+)?\s*[-+/*]\s*\d+(\.\d+)?(?:\s*[-+/*]\s*\d+(\.\d+)?)*|\([^)]*\))'
    text = re.sub(equation_pattern, '[EQUATION]', text)
    return text

def remove_duplicate_titles(text):
    title_pattern = r'(?i)chapter\s*\d+\s*[:\-]?\s*[a-z\s]*'
    text = re.sub(title_pattern, '', text)
    return text

def merge_broken_sentences(text):
    text = re.sub(r'(?<!\.\s|\?\s|\!\s)\n', ' ', text)
    return text

def remove_repeated_phrases(text):
    repeated_pattern = r'(?i)test bank for kimmel.*'
    text = re.sub(repeated_pattern, '', text)
    return text

def normalize_text_formatting(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[\*\-\•]\s+', '- ', text)
    return text

def clean_text(text):
    text = remove_headers_footers(text)
    text = remove_special_characters(text)
    text = remove_mcq_options(text)
    text = remove_numbering(text)
    text = replace_equations(text)
    text = remove_duplicate_titles(text)
    text = merge_broken_sentences(text)
    text = remove_repeated_phrases(text)
    text = normalize_text_formatting(text)
    return text.strip()

def load_and_clean_pdfs(pdf_dir):
    all_documents = []
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, filename)
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()

            for doc in documents:
                cleaned_text = clean_text(doc.page_content)
                cleaned_doc = Document(page_content=cleaned_text, metadata=doc.metadata)
                all_documents.append(cleaned_doc)
    return all_documents

def save_chunks_to_json(chunks, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for i, chunk in enumerate(chunks):
        file_path = os.path.join(output_dir, f'chunk_{i}.json')
        with open(file_path, 'w') as f:
            json.dump({"content": chunk.page_content, "metadata": chunk.metadata}, f)

def main(pdf_dir, output_dir, chunk_size, chunk_overlap):
    cleaned_documents = load_and_clean_pdfs(pdf_dir)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(cleaned_documents)
    save_chunks_to_json(chunks, output_dir)
    print(f"Total documents cleaned: {len(cleaned_documents)}")
    print(f"Chunks saved to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process PDFs and split them into text chunks.")
    parser.add_argument("--input_dir", type=str, required=True, help="Directory containing PDF files.")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save output JSON files.")
    parser.add_argument("--chunk_size", type=int, default=1000, help="Size of each chunk.")
    parser.add_argument("--chunk_overlap", type=int, default=200, help="Overlap size between chunks.")
    args = parser.parse_args()

    main(args.input_dir, args.output_dir, args.chunk_size, args.chunk_overlap)
