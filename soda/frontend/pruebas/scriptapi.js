// Reemplaza 'YOUR_API_KEY' con tu clave API real
const apiKey = '8C6ZGUKLBIQ36UEO';
const symbol = 'AAPL'; // Símbolo de la acción
const interval = '5min'; // Intervalo de tiempo para los datos
const url = `https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=${symbol}&interval=${interval}&apikey=${apiKey}`;

// Hacer la petición fetch
fetch(url)
  .then(response => response.json())  // Convierte la respuesta a formato JSON
  .then(data => {
    // Accede a los datos de Time Series y transforma la respuesta
    const timeSeries = data['Time Series (5min)'];

    // Crear el array con los datos transformados
    const formattedData = Object.keys(timeSeries).map(time => {
      return {
        time: time.split(' ')[0], // Solo la fecha
        value: parseFloat(timeSeries[time]['4. close']) // Precio de cierre
      };
    });

    console.log(formattedData); // Mostrar los datos formateados
  })
  .catch(error => {
    console.error('Error al obtener los datos:', error);
  });

