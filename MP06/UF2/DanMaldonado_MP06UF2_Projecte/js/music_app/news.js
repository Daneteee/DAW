export async function fetchSongNews(songName, artistName, NEWS_API_KEY) {
    // Definim les cerques que realitzarem per obtenir notícies sobre la cançó i l'artista
    const searchQueries = [
        `"${artistName}"`,  
        `"${songName}" música`, 
        `${artistName} música`,  
        `concierto "${artistName}"`, 
        `música "${songName}"` 
    ];

    let allArticles = [];

    // Recorrerem totes les cerques definides
    for (const query of searchQueries) {
        try {
            // Realitzem la petició a l'API de notícies amb la cerca corresponent
            const response = await fetch(`https://newsapi.org/v2/everything?q=${encodeURIComponent(query)}&apiKey=${NEWS_API_KEY}&language=es&pageSize=10&sortBy=publishedAt`, {
                headers: {
                    'User-Agent': 'MusicNewsApp/1.0'
                }
            });

            // Convertim la resposta a JSON
            const data = await response.json();

            // Filtrem els articles per eliminar els duplicats
            const filteredArticles = data.articles.filter(article => {

                // Comprovem si l'article ja existeix a la llista
                const isDuplicate = allArticles.some(existing => 
                    existing.title === article.title || existing.url === article.url
                );

                // Comprovem si l'article és rellevant
                const isRelevant = 
                    article.title.toLowerCase().includes(artistName.toLowerCase()) ||
                    article.description?.toLowerCase().includes(artistName.toLowerCase()) ||
                    article.title.toLowerCase().includes(songName.toLowerCase()) ||
                    article.description?.toLowerCase().includes(songName.toLowerCase());

                // Retornem l'article només si no és duplicat i és rellevant
                return !isDuplicate && isRelevant;
            });

            // Afegim els articles a la llista general d'articles
            allArticles = [...allArticles, ...filteredArticles];

            // Si hem trobat 5 articles, aturem la cerca
            if (allArticles.length >= 5) break;

        } catch (error) {
            // Si hi ha un error en la petició, el mostrem per consola
            console.error('Error buscant notícies:', error);
        }
    }

    // Retornem els 5 primers articles trobats
    return allArticles.slice(0, 5);
}
