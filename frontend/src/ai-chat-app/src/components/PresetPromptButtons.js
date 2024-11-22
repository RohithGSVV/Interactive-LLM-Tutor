// src/components/PresetPromptButtons.js
import React, { useState, useEffect } from 'react';
import './PresetPromptButtons.css';
import chaptersData from '../data/chapters.json'; // Adjust the path based on your folder structure

const PresetPromptButtons = ({ onPresetClick }) => {
  const [chapters, setChapters] = useState([]);

  // Load chapters from the JSON file (or other source)
  useEffect(() => {
    setChapters(chaptersData.chapters); // Set the chapters state when the component is mounted
  }, []);

  // State to manage which chapter is expanded, null means all chapters are closed
  const [expandedChapter, setExpandedChapter] = useState(0); // useState(null);

  // Toggle the chapter expansion
  const toggleChapter = (index) => {
    setExpandedChapter(expandedChapter === index ? null : index);
  };

  return (
    <div className="preset-prompt-tree">
      <h2 className="chapters-heading">Chapters</h2>
      {chapters.map((chapter, index) => (
        <div key={index} className="chapter">
          <button
            className="chapter-button"
            onClick={() => toggleChapter(index)}
          >
            {chapter.title}
          </button>
          {expandedChapter === index && (
            <div className="questions">
              {chapter.questions.map((question, qIndex) => (
                <button
                  key={qIndex}
                  className="prompt-button"
                  onClick={() => onPresetClick(question)}
                >
                  {question}
                </button>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default PresetPromptButtons;
