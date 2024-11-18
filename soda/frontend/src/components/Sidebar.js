import React from 'react';
import { Wallet, TrendingUp, PieChart, Bell, Settings, Menu, X } from 'lucide-react';

const menuItems = [
  { icon: Wallet, label: 'Cartera', id: 'portfolio' },
  { icon: TrendingUp, label: 'Mercados', id: 'markets' },
  { icon: PieChart, label: 'Análisis', id: 'analysis' },
];

export default function Sidebar({ isOpen, toggleSidebar, activeTab, setActiveTab }) {
  return (
    <div className={`fixed top-0 left-0 h-full bg-white shadow-lg transition-all duration-300 ease-in-out z-50 
      ${isOpen ? 'w-64' : 'w-16'}`}>
      
      <div className="p-4 flex items-center justify-between">
        {isOpen && <span className="text-xl font-bold text-violet-600">InvestApp</span>}
        <button onClick={toggleSidebar} className="p-2 hover:bg-gray-100 rounded-lg">
          {isOpen ? <X className="w-6 h-6 text-gray-600" /> : <Menu className="w-6 h-6 text-gray-600" />}
        </button>
      </div>

      <div className="mt-8 space-y-2">
        {menuItems.map((item) => (
          <button
            key={item.id}
            onClick={() => setActiveTab(item.id)}
            className={`w-full flex items-center p-4 space-x-4 hover:bg-violet-50 transition-colors
              ${activeTab === item.id ? 'text-violet-600 bg-violet-50' : 'text-gray-600'}`}
          >
            <item.icon className="w-6 h-6" />
            {isOpen && <span>{item.label}</span>}
          </button>
        ))}
      </div>

      <div className="absolute bottom-8 w-full space-y-2">
        {[{ icon: Bell, label: 'Notificaciones' }, { icon: Settings, label: 'Ajustes' }].map((item, index) => (
          <button
            key={index}
            className="w-full flex items-center p-4 space-x-4 hover:bg-violet-50 text-gray-600 transition-colors"
          >
            <item.icon className="w-6 h-6" />
            {isOpen && <span>{item.label}</span>}
          </button>
        ))}
      </div>
    </div>
  );
}
