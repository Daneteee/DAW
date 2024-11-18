import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Card, CardHeader, CardTitle, CardContent } from './Card.js';
import { stockData } from '../data/stockData.js';

export default function StockChart() {
  return (
    <Card className="col-span-full">
      <CardHeader>
        <CardTitle>Apple Inc. (AAPL)</CardTitle>
      </CardHeader>
      <CardContent className="p-4">
        <div style={{ width: '100%', height: '200px' }}>
          <ResponsiveContainer>
            <LineChart data={stockData}>
              <XAxis dataKey="time" />
              <YAxis />
              <CartesianGrid strokeDasharray="3 3" vertical={false} />
              <Tooltip />
              <Line type="monotone" dataKey="price" stroke="#8b5cf6" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  );
}
