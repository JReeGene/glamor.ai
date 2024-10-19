'use client'
import React from 'react'
import { useState, useEffect } from 'react'

export default function DarkMode() {
  const [theme, setTheme] = useState('light');
  useEffect(() => {
    // Check the local storage or system preference for theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      setTheme(savedTheme);
      document.documentElement.setAttribute('data-theme', savedTheme);
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      setTheme('dark');
      document.documentElement.setAttribute('data-theme', 'dark');
    }
  }, []);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
  };
  return (
      <div className="fixed top-4 right-4 md:top-6 md:right-6 z-50 flex items-center space-x-4">
          {/* Dark/Light Mode Toggle Button */}
         <button
            className="p-2 bg-blue-500 text-white rounded-full text-sm"
           onClick={toggleTheme}
          >
            {theme === 'light' ? '🌙 Dark' : '☀️ Light'}
        </button>
      </div>   
  )
}
