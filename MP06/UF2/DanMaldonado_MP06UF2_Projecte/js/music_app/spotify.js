import { searchTracks } from './spotifySearch.js';
import { fetchSongNews } from './news.js';  
import { createTrackModal, createNewsModal } from './modals.js';  

// Definim les claus d'API de Spotify i de notícies
const CLIENT_ID = 'c011d9f60c134b8cbf866557251e2748';
const CLIENT_SECRET = 'a892e3137dd647afb3f5555e82a9e125';
const NEWS_API_KEY = 'c1b53b8f81c047a1adb4f94a64233a66';

// Funció per renderitzar les pistes de Spotify
export async function renderSpotifyTracks() {
    const mainContent = document.querySelector('.main-content');
    mainContent.innerHTML = ''; 

    // Contenidor per la cerca
    const searchContainer = document.createElement('div');
    searchContainer.style.display = 'flex';
    searchContainer.style.justifyContent = 'center';
    searchContainer.style.marginBottom = '20px';

    // Creem el camp d'entrada per la cerca
    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.placeholder = 'Buscar cançons...';
    searchInput.style.padding = '10px';
    searchInput.style.width = '300px';
    searchInput.style.borderRadius = '5px';
    searchInput.style.border = '1px solid var(--accent)';

    // Creem el botó de cerca
    const searchButton = document.createElement('button');
    searchButton.textContent = 'Buscar';
    searchButton.style.marginLeft = '10px';
    searchButton.style.padding = '10px 20px';
    searchButton.style.backgroundColor = 'var(--accent)';
    searchButton.style.color = 'white';
    searchButton.style.border = 'none';
    searchButton.style.borderRadius = '5px';
    searchButton.style.cursor = 'pointer';

    // Afegim el camp d'entrada i el botó al contenidor de cerca
    searchContainer.appendChild(searchInput);
    searchContainer.appendChild(searchButton);
    mainContent.appendChild(searchContainer);

    // Creem un contenidor per les pistes
    const tracksContainer = document.createElement('div');
    tracksContainer.classList.add('spotify-tracks');
    tracksContainer.style.display = 'flex';
    tracksContainer.style.flexWrap = 'wrap';
    tracksContainer.style.gap = '20px';
    tracksContainer.style.justifyContent = 'center';

    // Renderitzem les pistem amb "Guns N' Roses" per defecte
    async function displayTracks(query = "Guns N' Roses") {
        tracksContainer.innerHTML = '';

        try {
            // Obtenim les pistes de Spotify
            const tracks = await searchTracks(query, CLIENT_ID, CLIENT_SECRET);

            // Limitem a 15 pistes
            const limitedTracks = tracks.slice(0, 15);

            // Creem la targeta amb la informació
            limitedTracks.forEach(track => {
                const trackCard = document.createElement('div');
                trackCard.style.width = '250px';
                trackCard.style.padding = '15px';
                trackCard.style.backgroundColor = 'var(--secondary)';
                trackCard.style.borderRadius = '10px';
                trackCard.style.textAlign = 'center';
                trackCard.style.color = 'var(--text)';
                trackCard.style.display = 'flex';
                trackCard.style.flexDirection = 'column';
                trackCard.style.alignItems = 'center';

                // Imatge de l'àlbum
                const albumImage = document.createElement('img');
                albumImage.src = track.album.images[0].url;
                albumImage.style.width = '200px';
                albumImage.style.height = '200px';
                albumImage.style.marginBottom = '1em';
                albumImage.style.objectFit = 'cover';
                albumImage.style.borderRadius = '10px';

                // Informació de la cancó
                const trackInfo = document.createElement('div');
                trackInfo.innerHTML = `
                    <h3>${track.name}</h3>
                    <p>Artista: ${track.artists[0].name}</p>
                    <p>Àlbum: ${track.album.name}</p>
                `;

                // Botó per veure notícies de la cançó
                const newsButton = document.createElement('button');
                newsButton.textContent = 'Veure noticies';
                newsButton.style.backgroundColor = 'var(--accent)';
                newsButton.style.marginTop = '1em';
                newsButton.style.color = 'white';
                newsButton.style.border = 'none';
                newsButton.style.padding = '10px 20px';
                newsButton.style.borderRadius = '5px';
                newsButton.style.cursor = 'pointer';

                // Busquem i mostrem noticies
                newsButton.addEventListener('click', async () => {
                    const songNews = await fetchSongNews(track.name, track.artists[0].name, NEWS_API_KEY);
                    createNewsModal(songNews, track.name); 
                });

                // Botó per veure els detalls
                const detailsButton = document.createElement('button');
                detailsButton.textContent = 'Llegir més';
                detailsButton.style.backgroundColor = 'var(--secondary)';
                detailsButton.style.marginTop = '1em';
                detailsButton.style.color = 'var(--text)';
                detailsButton.style.border = 'none';
                detailsButton.style.padding = '10px 20px';
                detailsButton.style.borderRadius = '5px';
                detailsButton.style.cursor = 'pointer';

                // Mostrem els detalls de la pista
                detailsButton.addEventListener('click', () => {
                    createTrackModal(track);  
                });

                trackCard.appendChild(albumImage);
                trackCard.appendChild(trackInfo);
                trackCard.appendChild(newsButton);
                trackCard.appendChild(detailsButton);

                tracksContainer.appendChild(trackCard);
            });

            // Afegim el contenidor de pistes a la pàgina
            mainContent.appendChild(tracksContainer);

        } catch (error) {
            console.error('Error en obtenir tracks:', error);
            tracksContainer.innerHTML = '<p>Error en carregar les cançons</p>';  
        }
    }

    // Event al botó de cerca
    searchButton.addEventListener('click', () => {
        const searchQuery = searchInput.value.trim();
        if (searchQuery) {

            // Realitzem la cerca amb el terme introduït
            displayTracks(searchQuery);
        }
    });

    // Permetem cercar amb la tecla Enter
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const searchQuery = searchInput.value.trim();
            if (searchQuery) {
                displayTracks(searchQuery); 
            }
        }
    });

    // Carreguem les pistes inicials
    await displayTracks();
}

// Afegim el full d'estils
const link = document.createElement('link');
link.rel = 'stylesheet';
link.href = '/css/music.css';
document.head.appendChild(link);

renderSpotifyTracks();
