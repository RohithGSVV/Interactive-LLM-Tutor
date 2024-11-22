// src/components/ModeSelector.js
import React from 'react';
import './ModeSelector.css';
import knowledgeIcon from './add-ons/knowledge-icon.jpg';
import quizzingIcon from './add-ons/quizzing-icon.jpg';
import problemSolvingIcon from './add-ons/problem-solving-icon.jpg';

const ModeSelector = ({ currentMode, onModeChange }) => {
  return (
    <div className="mode-selector">
      <label>Select Mode: </label>
      <select value={currentMode} onChange={(e) => onModeChange(e.target.value)}>
        <option value="knowledge">Knowledge Mode</option>
        <option value="quizzing">Quizzing Mode</option>
        <option value="problem-solving">Problem Solving</option>
      </select>
      <div className="mode-icons">
        <img
          src={currentMode === 'knowledge' ? knowledgeIcon : currentMode === 'quizzing' ? quizzingIcon : problemSolvingIcon}
          alt="Mode Icon"
          className="mode-icon"
        />
      </div>
    </div>
  );
};

export default ModeSelector;
