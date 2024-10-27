document.addEventListener('DOMContentLoaded', () => {
    
    // Inicialitzem variables i constants
    const modeButton = document.getElementById('mode-button');
    const playButton = document.querySelector('.play-button');
    const timerMinutes = document.querySelector('.minutes');
    const timerSeconds = document.querySelector('.seconds');
    let intervalId; // ID del temporizador per aturar-lo
    let timeLeft;
    let gameEnded = false;
    
    // Dificultats
    const difficulties = {
        "30seg": 30,
        "1min": 60,
        "2min": 120,
        "3min": 180,
        "5min": 300
    };
    const difficultyKeys = Object.keys(difficulties);
    let currentDifficultyIndex = 0; 
    
    // Cartes
    const cards = [
        'static/icons/big-bread.png', 
        'static/icons/bimbo.png', 
        'static/icons/bread.png', 
        'static/icons/cake.png', 
        'static/icons/waffle.png', 
        'static/icons/pancake.png', 
        'static/icons/macaron.png', 
        'static/icons/flan.png', 
        'static/icons/cupcake.png', 
        'static/icons/croissant.png', 
        'static/icons/cookie.png', 
        'static/icons/cinnamon.png'
    ];

    // Afegim cartes barrejades 2 cops i barregem el resultat
    const shuffledCards = shuffleArray([...shuffleArray([...cards]), ...shuffleArray([...cards])]);

    let flippedCards = [];
    let matchedPairs = 0;
    
    // Inicialitzem el tauler
    const gameGrid = document.getElementById('gameGrid');

    
    
    // Canviem la dificultat en clicar el botó de Temps
    modeButton.addEventListener('click', () => {
        
        //Rotem entre dificultats
        currentDifficultyIndex = (currentDifficultyIndex + 1) % difficultyKeys.length;
        const currentKey = difficultyKeys[currentDifficultyIndex];
        modeButton.textContent = `Temps: ${currentKey}`;
    });

    // Iniciem el joc quan cliquem al botó de jugar
    playButton.addEventListener('click', startGame);

    function startGame() {
        // Ocultem el titol principal
        document.querySelector('.main-title').style.display = 'none';
        
        // Mostrem el joc i el logo
        document.querySelector('.game').style.display = 'block';
        document.querySelector('.game .logo').style.top = '1em';

        // Iniciem temporitzador
        const currentKey = difficultyKeys[currentDifficultyIndex];
        timeLeft = difficulties[currentKey]; // El temps segons la dificultat seleccionada
        updateTimerDisplay();
        startTimer();
    }

    // Iniciem temporitzador
    function startTimer() {
        // Limpiar cualquier temporizador anterior
        clearInterval(intervalId);
    
        // Actualitzem el comptador cada segon
        intervalId = setInterval(() => {

            // Si el temps s'ha acabat donem per perduda la partida i donem la volta a les cartes
            if (timeLeft <= 0) {
                clearInterval(intervalId); // Aturem el temporitzador
                alert("S'ha acabat el temps!!");
                gameEnded = true;
                flipAllCards();
                return; 
            }
    
            timeLeft--; // Anem reduint el temps
            updateTimerDisplay(); // Actualitzem els minuts i segons
        }, 1000);
    }

    // Funcio per actualitzar el temps
    function updateTimerDisplay() {
        // Calculem els minuts restants dividint el temps restant en segons per 60
        const minutes = Math.floor(timeLeft / 60);
        // Calculem els segons restants utilitzant l'operador de mòdul amb 60
        const seconds = timeLeft % 60;
        
        // Actualitzem el contingut de l'element que mostra els minuts y figuem que siguin 2 digits
        timerMinutes.textContent = String(minutes).padStart(2, '0');
        timerSeconds.textContent = String(seconds).padStart(2, '0');
    }

    // Algorisme de Fisher-Yates
    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.round(Math.random() * i);
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }


    // Creem la carta
    function createCard(card, index) {

        // Creem l'element de la carta
        const cardElement = document.createElement('div');
        cardElement.className = 'card';
        cardElement.dataset.index = index;
        cardElement.innerHTML = `
            <div class="card-inner">
                <div class="card-front"></div>
                <div class="card-back">
                    <img src="${card}" alt="card" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
            </div>`;
        return cardElement; 
    }

    // Donar la volta a totes les cartes
    function flipAllCards() {
        
        // En cas que s'hagi perdut donem la volta a totes les cartes
        document.querySelectorAll('.card').forEach(card => {
            if (!card.classList.contains('flipped')) {
                card.classList.add('flipped');
            }
        });
    }
    
    // Creem el tauler de joc
    function createGrid() {
        shuffledCards.forEach((card, index) => {

            // Afegim la carta al tauler
            gameGrid.appendChild(createCard(card, index));
        });
    }

    // Funció per donar la volta a una carta
    function flipCard(card) {
        // Comprovem que no hi hagi més de 2 cartes voltejadas, que no estiguin ya voltejades (flipped o matched) i que no hagi acabat el joc
        if (flippedCards.length < 2 && !card.classList.contains('flipped') && !card.classList.contains('matched') && !gameEnded) {
            
            // Donem la volta a la carta i l'afegim a flippedCards
            card.classList.add('flipped');
            flippedCards.push(card);
            
            // Comprovem que les cartes siguin iguals i donem la volta després d'1 segon en cas que no ho siguin
            if (flippedCards.length === 2) {
                setTimeout(checkMatch, 1000);
            }
        }
    }

    // Comprovem si les cartes són iguals
    function checkMatch() {

        // Asignem un valor de flippedCards a cada la carta corresponent
        let [card1, card2] = flippedCards;

        // Comprovem que sigui la mateixa carta
        let isMatch = card1.querySelector('.card-back img').src === card2.querySelector('.card-back img').src;

        // En cas que ho sigui les deixem com a "matched" i afegim 1 al comptador
        if (isMatch) {
            card1.classList.add('matched');
            card2.classList.add('matched');
            matchedPairs++;

            // Si el comptador arriba a la longitud total de les cartes vol dir que el jugador ha guanyat
            if (matchedPairs === cards.length) {
                clearInterval(intervalId); // Aturem el temporitzador
                setTimeout(() => alert('Felicitats! Has guanyat!! :D'));
            }
        } else {
            // En cas que no siguin iguals les tornem a voltejar
            card1.classList.remove('flipped');
            card2.classList.remove('flipped');
        }

        // Buidem flippedCards
        flippedCards = [];
    }

    // Creem el tauler
    createGrid();

    // Donem la volta a la carta
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', () => flipCard(card));
    });

    // Obrim el pop up de sortir
    document.querySelector('.exit-button').addEventListener('click', () => {
        document.querySelector('.exit').style.display = 'flex';
    });

    // En cas que diguem que si, tornem al menu principal
    document.querySelector('.exit-yes').addEventListener('click', () => {
        document.querySelector('.game').style.display = 'none';
        document.querySelector('.main-title').style.display = 'flex';

    });

    // En cas que no, tanquem el pop up
    document.querySelector('.exit-no').addEventListener('click', () => {
        document.querySelector('.exit').style.display = 'none';
    });
});
