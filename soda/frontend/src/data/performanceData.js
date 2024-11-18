function generatePerformanceData(type) {
  const now = new Date();
  const data = [];

  switch(type) {
      case 'daily':
          // Genera datos para los últimos 14 días
          for (let i = 14; i >= 0; i--) {
              const date = new Date(now);
              date.setDate(now.getDate() - i);
              data.push({
                  time: date.toISOString().split('T')[0],
                  value: 100 + Math.random() * 50
              });
          }
          break;
      
      case 'weekly':
          // Genera datos para las últimas 8 semanas (7 * 7 días)
          for (let i = 7; i >= 0; i--) {
              const date = new Date(now);
              date.setDate(now.getDate() - (i * 7));
              data.push({
                  time: date.toISOString().split('T')[0],
                  value: 100 + Math.random() * 100
              });
          }
          break;
      
      case 'monthly':
          // Genera datos para los últimos 6 meses
          for (let i = 5; i >= 0; i--) {
              const date = new Date(now);
              date.setMonth(now.getMonth() - i);
              date.setDate(1);
              data.push({
                  time: date.toISOString().split('T')[0],
                  value: 100 + Math.random() * 150
              });
          }
          break;

      case 'anual':
          // Genera datos para los últimos 5 años
          for (let i = 5; i >= 0; i--) {
              const date = new Date(now);
              date.setFullYear(now.getFullYear() - i);
              date.setMonth(0); // Enero
              date.setDate(1);
              data.push({
                  time: date.toISOString().split('T')[0],
                  value: 100 + Math.random() * 200
              });
          }
          break;

          case 'total':
            // Usa la fecha actual para 'Total'
            data.push({
                time: now.toISOString().split('T')[0], // Usa la fecha actual
                value: 100 + Math.random() * 500
            });
            break;
        
  }
  
  return data;
}


// Exportar las funciones de datos generados para cada tipo
export const dailyData = generatePerformanceData('daily');
export const weeklyData = generatePerformanceData('weekly');
export const monthlyData = generatePerformanceData('monthly');
export const yearlyData = generatePerformanceData('anual');
export const allData = generatePerformanceData('total');

