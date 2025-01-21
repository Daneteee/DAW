export function createUserForm() {

    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = '/css/form.css'; 
    document.head.appendChild(link);

    const mainContent = document.querySelector('.main-content');
    mainContent.innerHTML = `
        <form id="userForm">
            <div class="form-group">
                <label for="fullName">Nom i Cognoms:</label>
                <input type="text" id="fullName" name="fullName" required>
                <div id="fullNameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="gender">Gènere:</label>
                <select id="gender" name="gender" required>
                    <option value="">Selecciona un gènere</option>
                    <option value="male">Home</option>
                    <option value="female">Dona</option>
                    <option value="other">No binari</option>
                </select>
                <div id="genderError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="birthDate">Data de Naixement:</label>
                <input type="date" id="birthDate" name="birthDate" required>
                <div id="birthDateError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="age">Edat:</label>
                <input type="number" id="age" name="age" readonly>
            </div>

            <button type="submit" id="submitBtn" disabled>Enviar</button>
            <div id="resultMessage"></div>
        </form>
    `;

    const form = document.getElementById('userForm');
    const fullNameInput = document.getElementById('fullName');
    const emailInput = document.getElementById('email');
    const genderSelect = document.getElementById('gender');
    const birthDateInput = document.getElementById('birthDate');
    const ageInput = document.getElementById('age');
    const submitBtn = document.getElementById('submitBtn');
    const resultMessage = document.getElementById('resultMessage');

    // Validació de nom i cognoms
    const fullNameRegex = /^[a-zA-Zàèìòùáéíóúäëïöüâêîôûçñ\s\.·]+$/u;
    fullNameInput.addEventListener('blur', () => {
        const fullNameError = document.getElementById('fullNameError');
        if (!fullNameRegex.test(fullNameInput.value.trim())) {
            fullNameInput.classList.add('invalid');
            fullNameError.textContent = 'El nom només pot contenir lletres, espais i alguns signes de puntuació';
        } else {
            fullNameInput.classList.remove('invalid');
            fullNameError.textContent = '';
        }
        checkFormValidity();
    });

    // Validació del email
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    emailInput.addEventListener('blur', () => {
        const emailError = document.getElementById('emailError');
        if (!emailRegex.test(emailInput.value.trim())) {
            emailInput.classList.add('invalid');
            emailError.textContent = 'Format d\'email no vàlid';
        } else {
            emailInput.classList.remove('invalid');
            emailError.textContent = '';
        }
        checkFormValidity();
    });

    // Validació de gènere
    genderSelect.addEventListener('change', () => {
        const genderError = document.getElementById('genderError');
        const validGenders = ['male', 'female', 'other'];
        if (!validGenders.includes(genderSelect.value)) {
            genderSelect.classList.add('invalid');
            genderError.textContent = 'Selecciona un gènere vàlid';
        } else {
            genderSelect.classList.remove('invalid');
            genderError.textContent = '';
        }
        checkFormValidity();
    });

    // Càlcul d'edat
    birthDateInput.addEventListener('change', () => {
        const birthDate = new Date(birthDateInput.value);
        const today = new Date();
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();
        
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }

        ageInput.value = age;
        checkFormValidity();
    });

    // Funció per comprovar la validesa del formulari
    function checkFormValidity() {
        const isFullNameValid = fullNameRegex.test(fullNameInput.value.trim());
        const isEmailValid = emailRegex.test(emailInput.value.trim());
        const isGenderValid = ['male', 'female', 'other'].includes(genderSelect.value);
        const isBirthDateValid = birthDateInput.value !== '';

        if (isFullNameValid && isEmailValid && isGenderValid && isBirthDateValid) {
            submitBtn.disabled = false;
            submitBtn.classList.add('active');
        } else {
            submitBtn.disabled = true;
            submitBtn.classList.remove('active');
        }
    }

    // Enviament del formulari
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        try {
            const response = await fetch('https://dummyjson.com/users/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    firstName: fullNameInput.value.split(' ')[0],
                    lastName: fullNameInput.value.split(' ').slice(1).join(' '),
                    email: emailInput.value,
                    gender: genderSelect.value,
                    age: parseInt(ageInput.value)
                })
            });

            if (response.ok) {
                resultMessage.style.color = 'green';
                resultMessage.textContent = 'Usuari donat d\'alta correctament';
                form.reset();
                submitBtn.disabled = true;
                submitBtn.classList.remove('active');
            } else {
                throw new Error('Error en donar d\'alta l\'usuari');
            }
        } catch (error) {
            resultMessage.style.color = 'red';
            resultMessage.textContent = 'Error en donar d\'alta l\'usuari';
        }
    });
}