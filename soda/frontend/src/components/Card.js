// src/components/ui/Card.js

import React from 'react';

export function Card({ children, className }) {
  return <div className={`bg-white rounded-lg shadow p-4 ${className}`}>{children}</div>;
}

export function CardHeader({ children }) {
  return <div className="border-b p-4">{children}</div>;
}

export function CardTitle({ children }) {
  return <h2 className="text-lg font-semibold">{children}</h2>;
}

export function CardContent({ children, className }) {
  return <div className={`p-4 ${className}`}>{children}</div>;
}
