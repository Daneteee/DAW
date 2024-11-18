import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from './Card.js';

export default function StocksCard() {
  return (
    <Card className="col-span-full lg:col-span-1">
      <CardHeader>
        <CardTitle>Acciones Destacadas</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div className="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
            <div>
              <div className="font-medium">AAPL</div>
              <div className="text-sm text-gray-500">Apple Inc.</div>
            </div>
            <div className="text-right">
              <div className="font-medium">€158.23</div>
              <div className="text-sm text-green-500">+2.4%</div>
            </div>
          </div>
          <div className="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
            <div>
              <div className="font-medium">GOOGL</div>
              <div className="text-sm text-gray-500">Alphabet Inc.</div>
            </div>
            <div className="text-right">
              <div className="font-medium">€2,830.45</div>
              <div className="text-sm text-red-500">-0.8%</div>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
