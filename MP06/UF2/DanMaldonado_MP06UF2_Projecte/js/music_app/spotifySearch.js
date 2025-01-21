import { getAccessToken } from './auth.js';

export async function searchTracks(query, CLIENT_ID, CLIENT_SECRET) {
    // Obtenim el token d'accés
    const accessToken = await getAccessToken(CLIENT_ID, CLIENT_SECRET);

    // Realitzem la petició a l'API de Spotify 
    const response = await fetch(`https://api.spotify.com/v1/search?q=${encodeURIComponent(query)}&type=track&limit=50`, {
        headers: {
            'Authorization': `Bearer ${accessToken}` 
        }
    });

    const data = await response.json();

    return data.tracks.items;
}
