import React, {useEffect, useRef  } from 'react';
import './ChatInterface.css';
import botIcon from './add-ons/robot.png';
import userIcon from './add-ons/user.png';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

const ChatInterface = ({ messages, setMessages, currentMode, isTyping, inputValue, setInputValue, sendMessage }) => {
  const messagesEndRef = useRef(null);
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  
  // UseEffect to trigger scroll when messages state changes
  useEffect(scrollToBottom, [messages]);
  
  const handleSend = async () => {
    if (inputValue.trim() !== '') {
      setMessages([...messages, { text: inputValue, sender: 'user', mode: currentMode }]);
      setInputValue('');
      await sendMessage(inputValue);
    }
  };

  const handleClearChat = () => {
    setMessages([]);
  };

  const handleExportChat = () => {
    const chatContent = messages
      .map((msg) => `${msg.sender === 'user' ? 'User' : 'Bot'} (${msg.mode}): ${msg.text}`)
      .join('\n');
    const blob = new Blob([chatContent], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    let timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    link.download = `accounting_tutor_chat_${timestamp}.txt`;
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="chat-interface">
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <React.Fragment key={index}>
            <div className={`message ${msg.sender} ${msg.mode}`}>
              <img
                src={msg.sender === 'user' ? userIcon : botIcon}
                alt={msg.sender}
                className="message-avatar"
              />
              <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {msg.text}
              </ReactMarkdown>
            </div>
            {index < messages.length - 1 && <div className="message-divider" />}
          </React.Fragment>
        ))}
        {isTyping && (
          <div className="message bot">
{/* Bootstrap spinner for loading */}
<div className="spinner-border text-primary" role="status">
            </div>
          </div>
        )}
        <div ref={messagesEndRef} /> {/* Empty div to mark the bottom */}
      </div>

      <div className="chat-input">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Type your message..."
          style={{ borderRadius: '5px', boxShadow: '0 2px 5px rgba(0, 0, 0, 0.1)' }}
        />
        <button onClick={handleSend} className="send-button">
          Send
        </button>
      </div>
      <div className="chat-history-controls">
        <button title = "Clear Chat History" className="clear-button" onClick={handleClearChat}>Clear Chat</button>
        <button title = "Download a copy of the chat history" className="export-button" onClick={handleExportChat}>Export Chat</button>
      </div>
    </div>
  );
};

export default ChatInterface;