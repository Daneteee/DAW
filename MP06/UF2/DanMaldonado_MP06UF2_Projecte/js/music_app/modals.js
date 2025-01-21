// Funció para crear el modal amb la informació de la canço
export function createTrackModal(track) {
    const modal = document.createElement('div');
    modal.style.position = 'fixed';
    modal.style.top = '0';
    modal.style.left = '0';
    modal.style.width = '100%';
    modal.style.height = '100%';
    modal.style.backgroundColor = 'rgba(0,0,0,0.7)';
    modal.style.display = 'flex';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
    modal.style.zIndex = '1000';

    const modalContent = document.createElement('div');
    modalContent.style.backgroundColor = 'var(--background)';
    modalContent.style.padding = '30px';
    modalContent.style.borderRadius = '15px';
    modalContent.style.maxWidth = '500px';
    modalContent.style.width = '90%';
    modalContent.style.textAlign = 'center';
    modalContent.style.position = 'relative';

    const albumImage = document.createElement('img');
    albumImage.src = track.album.images[0].url;
    albumImage.style.width = '300px';
    albumImage.style.height = '300px';
    albumImage.style.objectFit = 'cover';
    albumImage.style.borderRadius = '15px';
    albumImage.style.marginBottom = '20px';

    const trackInfo = document.createElement('div');
    trackInfo.innerHTML = `
        <h2>${track.name}</h2>
        <p><strong>Artista:</strong> ${track.artists[0].name}</p>
        <p><strong>Àlbum:</strong> ${track.album.name}</p>
        <p><strong>Any de sortida:</strong> ${track.album.release_date || 'No disponible'}</p>
        <p><strong>Rating:</strong> ${track.popularity}/100</p>
    `;

    const closeButton = document.createElement('button');
    closeButton.textContent = 'Tancar';
    closeButton.style.backgroundColor = 'var(--accent)';
    closeButton.style.color = 'white';
    closeButton.style.border = 'none';
    closeButton.style.padding = '10px 20px';
    closeButton.style.borderRadius = '5px';
    closeButton.style.marginTop = '20px';
    closeButton.style.cursor = 'pointer';

    const spotifyLink = document.createElement('a');
    spotifyLink.href = track.external_urls.spotify;
    spotifyLink.textContent = 'Escoltar a Spotify';
    spotifyLink.target = '_blank';
    spotifyLink.style.display = 'inline-block';
    spotifyLink.style.backgroundColor = 'var(--secondary)';
    spotifyLink.style.color = 'var(--text)';
    spotifyLink.style.textDecoration = 'none';
    spotifyLink.style.padding = '10px 20px';
    spotifyLink.style.borderRadius = '5px';
    spotifyLink.style.margin = '0 10px';

    modalContent.appendChild(albumImage);
    modalContent.appendChild(trackInfo);
    modalContent.appendChild(spotifyLink);
    modalContent.appendChild(closeButton);

    modal.appendChild(modalContent);

    closeButton.addEventListener('click', () => {
        document.body.removeChild(modal);
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            document.body.removeChild(modal);
        }
    });

    document.body.appendChild(modal);
}

// Funció per crear el modal de les noticies
export function createNewsModal(news, songName) {

    // Modal
    const modal = document.createElement('div');
    modal.style.position = 'fixed';
    modal.style.top = '0';
    modal.style.left = '0';
    modal.style.width = '100%';
    modal.style.height = '100%';
    modal.style.backgroundColor = 'rgba(0,0,0,0.7)';
    modal.style.display = 'flex';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
    modal.style.zIndex = '1000';
    modal.style.overflowY = 'auto';
    modal.style.padding = '20px';

    // Contingut del modal
    const modalContent = document.createElement('div');
    modalContent.style.backgroundColor = 'var(--background)';
    modalContent.style.padding = '30px';
    modalContent.style.borderRadius = '15px';
    modalContent.style.maxWidth = '700px';
    modalContent.style.width = '90%';
    modalContent.style.maxHeight = '80%';
    modalContent.style.overflowY = 'auto';

    // Títol del modal
    const title = document.createElement('h2');
    title.textContent = `Noticies relacionades amb "${songName}"`;
    title.style.textAlign = 'center';
    title.style.marginBottom = '20px';

    // Noticies
    const newsContainer = document.createElement('div');
    newsContainer.style.display = 'flex';
    newsContainer.style.flexDirection = 'column';
    newsContainer.style.gap = '15px';

    // Comprovem que hi hagin noticies
    if (news.length === 0) {
        const noNewsMessage = document.createElement('p');
        noNewsMessage.textContent = "No s'han trobat noticies...";
        noNewsMessage.style.textAlign = 'center';
        newsContainer.appendChild(noNewsMessage);
    } else {
        
        // Creem la tageta amb la noticia
        news.forEach(article => {
            const newsCard = document.createElement('div');
            newsCard.style.backgroundColor = 'var(--secondary)';
            newsCard.style.padding = '15px';
            newsCard.style.borderRadius = '10px';
            newsCard.style.display = 'flex';
            newsCard.style.flexDirection = 'column';

            // Títol de la noticia
            const newsTitle = document.createElement('h3');
            newsTitle.textContent = article.title;
            newsTitle.style.marginBottom = '10px';

            // Descripció
            const newsDescription = document.createElement('p');
            newsDescription.textContent = article.description || 'No hi ha descripció disponible...';
            newsDescription.style.marginBottom = '10px';

            // Enllaç a la noticia completa
            const newsLink = document.createElement('a');
            newsLink.href = article.url;
            newsLink.textContent = 'Llegir la noticia completa.';
            newsLink.target = '_blank';
            newsLink.style.color = 'var(--accent)';
            newsLink.style.textDecoration = 'none';
            newsLink.style.alignSelf = 'flex-start';

            newsCard.appendChild(newsTitle);
            newsCard.appendChild(newsDescription);
            newsCard.appendChild(newsLink);

            newsContainer.appendChild(newsCard);
        });
    }

    // Botó de tancar
    const closeButton = document.createElement('button');
    closeButton.textContent = 'Cerrar';
    closeButton.style.backgroundColor = 'var(--accent)';
    closeButton.style.color = 'white';
    closeButton.style.border = 'none';
    closeButton.style.padding = '10px 20px';
    closeButton.style.borderRadius = '5px';
    closeButton.style.marginTop = '20px';
    closeButton.style.alignSelf = 'center';
    closeButton.style.cursor = 'pointer';

    modalContent.appendChild(title);
    modalContent.appendChild(newsContainer);
    modalContent.appendChild(closeButton);
    modal.appendChild(modalContent);

    // Events per tancar
    closeButton.addEventListener('click', () => {
        document.body.removeChild(modal);
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            document.body.removeChild(modal);
        }
    });

    document.body.appendChild(modal);
}