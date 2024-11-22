import React from 'react';
import './Header.css';
import logo from './add-ons/logo.png';

const Header = () => {
  return (
    <header className="header">
      <img src={logo} alt="Georgia State University" className="header-logo" />
      <div className="header-text">
        <h1>Accounting Tutor</h1>
        <p className="subtitle">Institute of Insight - School of Accountancy</p>
        <p className="subtitle">A Generative AI tool for Studying Accounting Principles</p>
      </div>
    </header>
  );
};

export default Header;
