import React, { useState } from 'react';
import Sidebar from '../components/Sidebar';
import BalanceCard from '../components/BalanceCard';
import InvestmentGraph from '../components/InvestmentGraph';
import StocksCard from '../components/StocksCard';
import StockChart from '../components/StockChart';

export default function InvestmentDashboard() {
  const [isOpen, setIsOpen] = useState(true);
  const [activeTab, setActiveTab] = useState('portfolio');

  return (
    <div className="flex">
      <Sidebar isOpen={isOpen} toggleSidebar={() => setIsOpen(!isOpen)} activeTab={activeTab} setActiveTab={setActiveTab} />

      <div className={`flex-1 min-h-screen p-6 ${isOpen ? 'ml-64' : 'ml-16'} transition-all`}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 lg:grid-cols-3">
          <BalanceCard />
          <InvestmentGraph />
          <StocksCard />
        </div>
      </div>
    </div>
  );
}
