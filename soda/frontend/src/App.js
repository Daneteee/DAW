// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import InvestmentDashboard from './pages/InvestmentDashboard';
import StockInfo from './pages/StockInfo';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<InvestmentDashboard />} />
        <Route path="/stock-info" element={<StockInfo />} />
        {/* Otras rutas que puedas tener */}
        {/* Ejemplo: <Route path="/other" element={<OtherComponent />} /> */}
        
        {/* Redirigir rutas desconocidas a InvestmentDashboard */}
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;
