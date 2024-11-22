import React, { useState, useEffect } from 'react';
import './Sidebar.css';
import PresetPromptButtons from './PresetPromptButtons';

const Sidebar = ({ currentMode, onModeChange , onPresetClick }) => {
  const [showSummary, setShowSummary] = useState(false);
  const [modeDescription, setModeDescription] = useState('');

  useEffect(() => {
    let description = '';
    switch (currentMode) {
      case 'knowledge':
        description = 'Knowledge Mode: Ideal for learning foundational concepts.';
        break;
      case 'quizzing':
        description = 'Quizzing Mode: Test your understanding with questions.';
        break;
      default:
        description = '';
    }
    setModeDescription(description);
    setShowSummary(true);

    const timer = setTimeout(() => {
      setShowSummary(false);
    }, 3000); // Show summary for 3 seconds

    return () => clearTimeout(timer);
  }, [currentMode]);

  return (
    <div className="sidebar">
      <h2>Options</h2>
      <div className="mode-selector">
        <label>Select Mode: </label>
        <select value={currentMode} onChange={(e) => onModeChange(e.target.value)}>
          <option value="knowledge">Knowledge Mode</option>
          <option value="quizzing">Quizzing Mode</option>
        </select>
      </div>
      {showSummary && (
        <div className={`mode-summary ${showSummary ? '' : 'hidden'}`}>
          {modeDescription}
        </div>
      )}
      <PresetPromptButtons onPresetClick={onPresetClick} />
    </div>
  );
};

export default Sidebar;
