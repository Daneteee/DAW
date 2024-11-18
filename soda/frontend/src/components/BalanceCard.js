import React from 'react';
import { Card, CardContent } from './Card.js';

export default function BalanceCard() {
  return (
    <Card className="col-span-full bg-gradient-to-r from-violet-600 to-indigo-600 text-white">
      <CardContent className="pt-6">
        <div className="text-sm opacity-80">Balance Total</div>
        <div className="text-4xl font-bold mt-2">€15,280.45</div>
        <div className="text-sm mt-2 opacity-80">+€234.23 (1.8%)</div>
      </CardContent>
    </Card>
  );
}
