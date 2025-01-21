export function setupClock() {

    const mainContent = document.querySelector('.main-content');
    
    mainContent.innerHTML = '';

    // Creem el contenidor del rellotge i apliquem estils
    const clockContainer = document.createElement('div');
    clockContainer.style.color = 'var(--text)';
    clockContainer.style.padding = '20px';
    clockContainer.style.borderRadius = '10px';
    clockContainer.style.margin = '20px auto';
    clockContainer.style.display = 'flex';
    clockContainer.style.flexDirection = 'column';
    clockContainer.style.alignItems = 'center';
    clockContainer.style.maxWidth = '400px';
    clockContainer.style.width = '100%';

    // Creem el títol
    const clockTitle = document.createElement('h2');
    clockTitle.textContent = 'Rellotge analògic i digital';
    clockTitle.style.marginBottom = '2em';
    clockTitle.style.color = 'black';

    // Creem els elements del rellotge
    const clockBody = document.createElement('div');
    clockBody.className = 'clock-body';

    // Contenidor de les hores
    const hours = document.createElement('div');
    hours.className = 'hours';

    // Creem els discs
    const discTop = document.createElement('div');
    discTop.className = 'disc disc-top';

    const discBottom = document.createElement('div');
    discBottom.className = 'disc disc-bottom';

    // Creem les agulles
    const secondHand = document.createElement('div');
    secondHand.className = 'hand second';

    const minuteHand = document.createElement('div');
    minuteHand.className = 'hand minute';

    const hourHand = document.createElement('div');
    hourHand.className = 'hand hour';

    // Creem el rellotge digital
    const digitalClock = document.createElement('div');
    digitalClock.className = 'digital-clock';
    digitalClock.style.marginTop = '20px';
    digitalClock.style.fontSize = '2rem';
    digitalClock.style.fontWeight = 'bold';
    digitalClock.style.color = 'var(--clr-dark)';

    // Creem els elements del rellotge
    clockBody.appendChild(hours);
    clockBody.appendChild(discTop);
    clockBody.appendChild(discBottom);
    clockBody.appendChild(secondHand);
    clockBody.appendChild(minuteHand);
    clockBody.appendChild(hourHand);

    // Afegim els elements al contenidor
    clockContainer.appendChild(clockTitle);
    clockContainer.appendChild(clockBody);
    clockContainer.appendChild(digitalClock);

    // L'afegim al main-content
    mainContent.appendChild(clockContainer);

    // Creem les marques d'hores i minuts
    for (let i = 1; i <= 60; i++) {
        if (i % 5 === 0) {
            const hourNumber = document.createElement('div');
            hourNumber.className = 'hour-number';
            const numberDiv = document.createElement('div');
            numberDiv.textContent = i / 5;
            hourNumber.appendChild(numberDiv);
            hourNumber.style.transform = `translateX(-50%) rotate(${i*6}deg)`;
            numberDiv.style.transform = `rotate(${i*-6}deg)`;
            hours.appendChild(hourNumber);
        } else {
            const minuteBar = document.createElement('div');
            minuteBar.className = 'minute-bar';
            minuteBar.style.transform = `translateX(-50%) rotate(${i*6}deg)`;
            hours.appendChild(minuteBar);
        }
    }

    // Formatem el temps del digital amb dos digits
    function formatTime(time) {
        return time.toString().padStart(2, '0');
    }

    // Funció per iniciar el rellotge
    function startClock() {
        const now = new Date();
        const seconds = now.getSeconds();
        const minutes = now.getMinutes();
        const hours = now.getHours();

        // Actualitzem el rellotge analògic
        let secDeg = seconds * (360 / 60) + minutes * 360;
        let minDeg = minutes * (360 / 60) + seconds / 12;
        let hourDeg = hours * (360 / 12) + (minutes / 12) * (360 / 60);
        
        secondHand.style.transform = `translateX(-50%) rotate(${secDeg}deg)`;
        minuteHand.style.transform = `translateX(-50%) rotate(${minDeg}deg)`;
        hourHand.style.transform = `translateX(-50%) rotate(${hourDeg}deg)`;

        // Actualitzem el rellotge digital
        digitalClock.textContent = `${formatTime(hours)}:${formatTime(minutes)}:${formatTime(seconds)}`;
    }

    // Afegim el full d'estils
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = '/css/clock.css';
    document.head.appendChild(link);

    // Iniciem els rellotges
    setInterval(startClock, 1000);
    startClock();
}