/**
 * Funció que obté informació sobre una ubicació a partir de les seves coordenades.
 * Realitza una sol·licitud a l'API PositionStack per convertir latitud i longitud en informació d'ubicació.
 * Si es troba informació, obté dades addicionals del país associat.
 * 
 * @param {number} lat - Latitud de la ubicació.
 * @param {number} lng - Longitud de la ubicació.
 * @returns {Promise<Object|null>} - Retorna les dades del país o `null` si no es pot determinar la ubicació.
 */
async function whereAmI(lat, lng) {
    const api_key = '7ed697284eb5074e81609346495ec635';
    const url = `http://api.positionstack.com/v1/reverse?access_key=${api_key}&query=${lat},${lng}`; 

    try {
        // Sol·licitud a l'API PositionStack
        const response = await fetch(url);
        if (!response.ok) throw new Error(`Error en la petició: ${response.status}`);

        // Convertimla resposta a JSON
        const data = await response.json();

        if (data.data && data.data.length > 0) {
            const location = data.data[0]; 
            const country_code = location.country_code; 

            // Mostrem la ubicació a la consola
            console.log(`Esteu a ${location.locality || 'desconeguda'}, ${location.country || 'desconegut'}`);

            // Retornem les dades del país
            return await getCountryData(country_code);
        } else {
            console.log('No s’ha pogut determinar la ubicació.');
            return null;
        }
    } catch (error) {
        console.error('Hi ha hagut un error:', error.message);
        return null;
    }
}

/**
 * Funció que obté informació detallada d'un país a partir del seu codi.
 * Fa servir l'API RestCountries per obtenir dades del país.
 * 
 * @param {string} country_code - Codi alfabètic de dues lletres del país.
 * @returns {Promise<Object|null>} - Retorna les dades del país o `null` si hi ha un error.
 */
async function getCountryData(country_code) {
    const url = `https://restcountries.com/v3.1/alpha/${country_code}`;
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`Error en la petició a l'API de països: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('Error en obtenir les dades del país:', error);
        return null;
    }
}

/**
 * Funció que genera una taula amb informació de països segons coordenades predefinides.
 * Mostra la bandera i dades del païs.
 */
async function displayCountries() {
    const tableBody = document.querySelector('#countryTable tbody');
    tableBody.innerHTML = ''; 

    const coordinates = [
        [52.508, 13.381], 
        [19.037, 72.873], 
        [-33.933, 18.474], 
    ];

    for (const [lat, lng] of coordinates) {
        const countryData = await whereAmI(lat, lng); 
        if (countryData && countryData.length > 0) {
            const country = countryData[0];

            const row = document.createElement('tr');

            // Cel·la amb la bandera del país
            const flag_cell = document.createElement('td');
            const country_flag = document.createElement('img');
            country_flag.src = country.flags.svg; 
            country_flag.alt = `Bandera de ${country.name.official}`;
            country_flag.style.width = '80px'; 
            flag_cell.appendChild(country_flag);
            row.appendChild(flag_cell);

            // Cel·la amb la informació del país
            const dataCell = document.createElement('td');
            dataCell.innerHTML = `
                <ul>
                    <li><strong>Nom oficial:</strong> ${country.name.official}</li>
                    <li><strong>Monedes:</strong> ${Object.values(country.currencies || {}).map(c => c.name).join(', ')}</li>
                    <li><strong>Idiomes:</strong> ${Object.values(country.languages || {}).join(', ')}</li>
                    <li><strong>Codi del país:</strong> ${country.cca2}</li>
                    <li><strong>Capital:</strong> ${country.capital ? country.capital[0] : 'Desconeguda'}</li>
                    <li><strong>Habitants:</strong> ${country.population.toLocaleString()}</li>
                    <li><strong>Fronteres:</strong> ${country.borders ? country.borders.join(', ') : 'Cap o no informades'}</li>
                    <li><strong>Zones horàries:</strong> ${country.timezones.join(', ')}</li>
                </ul>
            `;
            row.appendChild(dataCell);

            tableBody.appendChild(row);
        }
    }
}

document.getElementById('getLocationButton').addEventListener('click', displayCountries);
