import React, { useState} from 'react';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import Sidebar from './components/Sidebar';
import ChatInterface from './components/ChatInterface';
//import PresetPromptButtons from './components/PresetPromptButtons';
//const endpoint = 'http://10.230.100.212:17029/v1/chat/completions';
const endpoint = process.env.REACT_APP_OLLAMA_BASE_URL;
const ai_application_url = `${process.env.REACT_APP_AI_APPLICTATION_BASE_URL}/v1/chat/completions`;
const ai_application_name = process.env.REACT_APP_AI_APPLICTATION_NAME;


function dashToTitle(str) {
  return str
    .split('-') // Split the string by underscores
    .map(word => word.length> 2 ? word.charAt(0).toUpperCase() + word.slice(1) : word.toUpperCase() ) // Capitalize the first letter of each word
    .join(' '); // Join the words with spaces
}


function App() {
  const [currentMode, setCurrentMode] = useState('knowledge');
  const [messages, setMessages] = useState([
    { text: "Welcome to Georgia State University's Accounting Tutor, powered by the Institute of Insight.", sender: 'bot', mode: 'knowledge' }
  ]);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [isTyping, setIsTyping] = useState(false);
  const [inputValue, setInputValue] = useState('');
  
  // document.title = dashToTitle(ai_application_name); /* https://stackoverflow.com/questions/34834091/changing-the-document-title-in-react */
  document.title = "Accounting Tutor";

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  const handlePresetClick = (prompt) => {
    setInputValue(prompt);
  };

  const sendMessage = async (message) => {
    if (!message.trim()) return;

    message = `Do not answer previous messages.  Only respond to the below message. The question is: ${message}`;

    if (currentMode === 'quizzing') {
      message = ` ${message} Ask 2 questions about the topics mentioned to the user.`;
    }

    const userMessage = { role: 'user', content: message };
    setInputValue('');
    setIsTyping(true);

    try {
      // const response = await fetch(endpoint, {
      const response = await fetch(ai_application_url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'llama3.1',
          messages: [
            ...messages.map(msg => ({
              role: msg.sender === 'bot' ? 'assistant' : 'user',
              content: msg.text
            })),
            userMessage
          ],
          stream: true,
        }),
      });

      const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let aiResponseContent = ''; // To accumulate the response content

  // Add a placeholder message to show the bot is typing
  setMessages((prevMessages) => [
    ...prevMessages,
    { text: aiResponseContent, sender: 'bot', mode: currentMode },
  ]);

  while (true) {
    const { done, value } = await reader.read();
    if (done) break; // Stop if the stream is done

    const chunk = decoder.decode(value);
    const lines = chunk.split('\n');

    for (const line of lines) {
      if (line.startsWith('data: ')) {
        const data = line.slice(6); // Remove "data: " prefix
        if (data === '[DONE]') {
          console.log('Stream finished');
          setIsTyping(false); // Hide the typing indicator
        } else {
          try {
            const parsed = JSON.parse(data);
            const content = parsed.choices[0].delta.content;

            if (content) {
              aiResponseContent += content; // Append new content

              // Efficiently update the last message in the state
              setMessages((prevMessages) => [
                ...prevMessages.slice(0, -1),
                { text: aiResponseContent, sender: 'bot', mode: currentMode },
              ]);
              console.log(aiResponseContent)
            }
            console.log(aiResponseContent); // Log the accumulated content
          } catch (error) {
            console.error('Error parsing JSON:', error);
          }
        }
      }
    }
      }
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: "An error occurred, please try again later", sender: 'bot', mode: currentMode },
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="App">
      <Header />
      <div className="app-body">
        <div className={`sidebar-toggle-container ${isSidebarOpen ? 'open' : 'closed'}`}>
          <button className="sidebar-toggle" onClick={toggleSidebar}>
            {isSidebarOpen ? '<<' : '>>'}
          </button>
        </div>
        {isSidebarOpen && (
          <Sidebar currentMode={currentMode} onModeChange={setCurrentMode} onPresetClick={handlePresetClick} />
        )}
        <div className={`main-content ${isSidebarOpen ? 'with-sidebar' : 'full-width'}`}>
          <ChatInterface
            messages={messages}
            setMessages={setMessages}
            currentMode={currentMode}
            isTyping={isTyping}
            inputValue={inputValue} // Pass input value to ChatInterface
            setInputValue={setInputValue} // Pass function to update input 
            sendMessage={sendMessage}
          />
        </div>
      </div>
      <Footer />
      <button className="floating-help-button" onClick={() => alert("Help is on the way!")}>?</button>
    </div>
  );
}

export default App;
