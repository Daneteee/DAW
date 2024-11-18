// src/pages/StockInfo.js

import React, { useState } from 'react';
import Sidebar from '../components/Sidebar';
import { Card, CardHeader, CardTitle, CardContent } from '../components/Card';
import InvestmentGraph from '../components/InvestmentGraph';
import { ArrowUpRight, Star, Share2 } from 'lucide-react';

// Simulación de datos de la empresa
const companyData = {
    name: "Amazon.com, Inc.",
    ticker: "AMZN",
    sector: "Tecnología",
    currentPrice: 135.12, // Precio ficticio; asegúrate de actualizarlo si necesitas datos en tiempo real
    priceChange: { amount: -2.16, percentage: -1.57 }, // Datos ficticios
    marketCap: "1.43T",
    peRatio: 62.7, // Ratio P/E ficticio; puede variar
    dividendYield: "N/A", // Amazon actualmente no tiene dividendos
  };
  

const StockInfo = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('portfolio');

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="flex">
      <Sidebar 
        isOpen={isSidebarOpen} 
        toggleSidebar={toggleSidebar}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />
      <div className={`flex-1 transition-all duration-300 ${isSidebarOpen ? 'ml-64' : 'ml-16'} bg-gray-50 min-h-screen p-6`}>
        
        <div className="m-5 gap-6 mt-6">
          <Card className="md:col-span-1">
            <CardHeader className="flex justify-between items-center">
              <div className="flex items-center space-x-4">
              <img 
                src="/amazon.svg" 
                alt="Amazon" 
                className="h-8  object-contain object-center"
              />

                <div>
                  <CardTitle>{companyData.name} ({companyData.ticker})</CardTitle>
                  <p className="text-sm text-gray-500">{companyData.sector}</p>
                </div>
              </div>
              <div className="flex space-x-2">
                <button className="p-2 bg-gray-100 rounded-full hover:bg-gray-200">
                  <Star className="text-yellow-500" />
                </button>
                <button className="p-2 bg-gray-100 rounded-full hover:bg-gray-200">
                  <Share2 className="text-gray-600" />
                </button>
              </div>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div>
                  <p className="text-sm text-gray-600">Precio Actual</p>
                  <h2 className="text-2xl font-bold text-green-600">${companyData.currentPrice}</h2>
                </div>
                <div>
                  <p className="text-sm text-gray-600">Cambio</p>
                  <div className="flex items-center">
                    <ArrowUpRight className="text-green-600 mr-2" />
                    <span className="text-green-600">+${companyData.priceChange.amount} ({companyData.priceChange.percentage}%)</span>
                  </div>
                </div>
                <InvestmentGraph />
                <Card className={"my-5"}>
                    <CardHeader>
                        <CardTitle>Accion</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="">
                        <button className="m-3 bg-green-500 text-white py-2 px-4 rounded-lg hover:bg-green-600 transition">
                            Comprar
                        </button>
                        <button className="m-3 bg-red-500 text-white py-2 px-4 rounded-lg hover:bg-red-600 transition">
                            Vender
                        </button>
                        </div>
                    </CardContent>
                </Card>
              </div> 
            </CardContent> 
          </Card>

          <Card className="md:col-span-1">
            <CardHeader>
              <CardTitle>Información de la Empresa</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                <div>
                  <p className="text-sm text-gray-600">Capitalización</p>
                  <p className="font-medium">{companyData.marketCap}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-600">P/E Ratio</p>
                  <p className="font-medium">{companyData.peRatio}</p>
                </div>
                <div>
                  <p className="text-sm text-gray-600">Rendimiento de Dividendos</p>
                  <p className="font-medium">{companyData.dividendYield}</p>
                </div>
              </div>
            </CardContent>
          </Card>

        </div>
      </div>
    </div>
  );
};

export default StockInfo;
