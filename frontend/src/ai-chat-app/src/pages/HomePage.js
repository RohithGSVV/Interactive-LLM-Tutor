// HomePage.js
import React, { useState } from 'react';
import ChatInterface from '../components/ChatInterface';
import PresetPromptButtons from '../components/PresetPromptButtons';
import ModeSelector from '../components/ModeSelector';

const HomePage = () => {
  const [currentMode, setCurrentMode] = useState('knowledge');
  const [messages, setMessages] = useState([]);

  const handlePresetClick = (prompt) => {
    setMessages((prevMessages) => [
      ...prevMessages,
      { text: prompt, sender: 'user' },
      { text: `You selected: ${prompt}`, sender: 'bot' }
    ]);
  };

  return (
    <div className="home-page">
      <ModeSelector currentMode={currentMode} onModeChange={setCurrentMode} />
      <PresetPromptButtons onPresetClick={handlePresetClick} />
      <ChatInterface messages={messages} setMessages={setMessages} />
    </div>
  );
};

export default HomePage;
