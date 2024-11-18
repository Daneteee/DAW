import React, { useEffect, useRef, useState } from 'react';
import { createChart } from 'lightweight-charts';
import { Card, CardHeader, CardTitle, CardContent } from './Card.js';
import { dailyData, weeklyData, monthlyData, yearlyData, allData} from '../data/performanceData.js'; // Asegúrate de tener estos datos

const PerformanceChart = () => {
    const chartContainerRef = useRef(null);
    const chartRef = useRef(null);
    const seriesRef = useRef(null);
    const [data, setData] = useState(dailyData); // Inicializar con datos diarios

    useEffect(() => {
        // Crear el gráfico
        chartRef.current = createChart(chartContainerRef.current, {
            layout: {
                textColor: 'black',
                background: { type: 'solid', color: 'white' },
            },
            rightPriceScale: {
                visible: true,
                borderColor: 'transparent',
            },
            leftPriceScale: {
                visible: false,
            },
            timeScale: {
                visible: true,
                borderColor: 'transparent',
            },
            handleScale: false,
            handleScroll: false,
            grid: {
                vertLines: { visible: false },
                horzLines: { visible: false },
            },
        });

        // Crear la serie de área
        seriesRef.current = chartRef.current.addAreaSeries({
            topColor: 'rgba(139, 92, 246, 0.2)',
            bottomColor: 'rgba(139, 92, 246, 0.05)',
            lineColor: 'rgba(139, 92, 246, 1)',
            lineWidth: 2,
        });

        // Establecer los datos iniciales
        seriesRef.current.setData(data);

        // Ajustar el contenido para mostrar todos los datos
        chartRef.current.timeScale().fitContent();

        // Limpieza
        return () => {
            if (chartRef.current) {
                chartRef.current.remove();
            }
        };
    }, []);

    useEffect(() => {
        if (!chartRef.current || !seriesRef.current) return;

        // Actualizar los datos de la serie
        seriesRef.current.setData(data);
        chartRef.current.timeScale().fitContent(); // Ajustar la escala de tiempo
    }, [data]);

    const handleTimeRangeChange = (range) => {
        switch (range) {
            case 'daily':
                setData(dailyData);
                break;
            case 'weekly':
                setData(weeklyData);
                break;
            case 'monthly':
                setData(monthlyData);
                break;
            
            case 'yearly':
                setData(yearlyData);
                break;
            
            case 'total':
                setData(allData);
                break;

            default:
                setData(dailyData);
        }
    };

    const renderTimeRangeButtons = () => {
        const ranges = [
            { label: 'Diario', value: 'daily' },
            { label: 'Semanal', value: 'weekly' },
            { label: 'Mensual', value: 'monthly' },
            { label: 'Anual', value: 'yearly' },
            { label: 'Todos', value: 'total' },
        ];

        return (
            <div className="flex space-x-2 mb-4">
                {ranges.map((range) => (
                    <button
                        key={range.value}
                        className={`px-4 py-2 rounded ${
                            data === (range.value === 'daily' ? dailyData : range.value === 'weekly' ? weeklyData : monthlyData) 
                                ? 'bg-purple-500 text-white' 
                                : 'bg-gray-200 text-gray-700'
                        }`}
                        onClick={() => handleTimeRangeChange(range.value)}
                    >
                        {range.label}
                    </button>
                ))}
            </div>
        );
    };

    return (
        <Card className="col-span-full lg:col-span-2">
            <CardHeader>
                <CardTitle>Rendimiento</CardTitle>
            </CardHeader>
            <CardContent className="p-4">
                {renderTimeRangeButtons()}
                <div style={{ width: '100%', height: '300px', position: 'relative' }}>
                    <div 
                        ref={chartContainerRef} 
                        style={{ 
                            width: '100%', 
                            height: '100%', 
                            position: 'absolute' 
                        }} 
                    />
                </div>
            </CardContent>
        </Card>
    );
};

export default PerformanceChart;