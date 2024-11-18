// components/NavBar.js
import React from 'react';
import { Bell, Settings } from 'lucide-react';

export default function NavBar({ isSidebarOpen }) {
  return (
    <nav className={`flex justify-between items-center bg-white shadow p-4 fixed top-0 left-0 right-0 z-40 transition-transform ${isSidebarOpen ? 'transform translate-x-64 md:translate-x-0' : ''}`}>
      <span className="text-xl font-bold text-violet-600">InvestApp</span>
      <div className="flex items-center space-x-4">
        <Bell className="w-6 h-6 text-gray-600 cursor-pointer hover:text-violet-600" />
        <Settings className="w-6 h-6 text-gray-600 cursor-pointer hover:text-violet-600" />
      </div>
    </nav>
  );
}
