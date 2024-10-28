let currentValue = "";
const inputScreen = document.querySelector('.screen');
let hasCalculated = true;
let history = [];
let seconds = 0;

// Afegim el valor a la pantalla
function addValue(value) {
    
    // Comprovem si hem calculat abans per netejar la pantalla en cas que fiquem un nombre nou
    if (hasCalculated && !["+","-","*","/"].includes(value)) {
        clearScreen();
        hasCalculated = false;
    }
    
    currentValue += value; 
    inputScreen.value = currentValue;
}


 
function calculate() {
    if (currentValue) {
        try {
            const result = eval(currentValue); 

            // Gestionem divisions entre 0
            if (result === Infinity || isNaN(result)) {
                inputScreen.value = "Math ERROR";
                currentValue = "";
            } else {

                // Afegim valor al historial i mostrem a la pantalla
                updateHistory(currentValue, result);

                inputScreen.value = result; 
                currentValue = result.toString();
                hasCalculated = true;
            }
        } catch (error) {
            // Gestionem errors de sintaxi
            inputScreen.value = "Syntax ERROR";
            currentValue = "";
        }
    }
}

// Netejem la pantalla
function clearScreen() {
    currentValue = "";
    inputScreen.value = "";
}

// Esborrar últim valor
function delValue() {
    currentValue = currentValue.slice(0, -1);
    inputScreen.value = currentValue;
}

// Actualitzem l'historial
function updateHistory(operation, result) {
    history.push(`${operation} = ${result}`);

    if (history.length > 2) {
        history.shift(); 
    }

    const historyDiv = document.getElementById('history');
    historyDiv.innerHTML = ''; 

    // Per cada element de l'historial fiquem una opacitat diferent
    history.forEach((item, index) => {
        const div = document.createElement('div');
        div.textContent = item;

        // Opacitat diferent per cada element
        const opacity = index === 0 ? 0.5 : 1; 
        div.style.opacity = opacity; 

        historyDiv.appendChild(div);
    });
}

// Actualitzem el temporitzador
function updateTimer() {
    seconds++;

    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;

    // Concatenem "0" si és menor de 10 per tenir 2 digits
    const hoursFormatted = (hours < 10 ? '0' : '') + hours;
    const minutesFormatted = (minutes < 10 ? '0' : '') + minutes;
    const secsFormatted = (secs < 10 ? '0' : '') + secs;

    document.getElementById('timer').innerText = 
        `${hoursFormatted}:${minutesFormatted}:${secsFormatted}`;
}

// Executem cada segon
setInterval(updateTimer, 1000);

// Utilitzant una funció anònima com a paràmetre criden al addEventListener
document.addEventListener('keydown', function(event) {
    const key = event.key;

    if (!isNaN(key) || key === '.') {
        addValue(key);
    } else if (key === '+' || key === '-' || key === '*' || key === '/') {
        addValue(key);
    } else if (key === 'Enter') {
        calculate();
    } else if (key === 'Backspace') {
        delValue();
    } else if (key === 'Escape') {
        clearScreen();
    }
});

