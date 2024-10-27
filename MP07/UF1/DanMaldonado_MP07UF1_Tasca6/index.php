<?php
session_start();

$errors = isset($_SESSION["errors"]) ? $_SESSION['errors'] : [];

session_unset();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulari</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            background: #d8b5ff;
        }
        .container {
            position: relative;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .form-container {
            background: rgba(255, 255, 255, 0.7);
            padding: 2em;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
            position: relative;
            z-index: 2;
        }
        h2 {
            color: #8a2be2;
            text-align: center;
            margin-bottom: 1em;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-top: 1em;
            color: #4b0082;
        }
        input, select {
            padding: 0.5em;
            margin-top: 0.5em;
            border: 1px solid #d8bfd8;
            border-radius: 5px;
            background-color: rgba(255,255,255,0.8);
        }
        input[type="submit"] {
            background-color: #9370db;
            color: white;
            padding: 0.7em;
            border: none;
            border-radius: 5px;
            margin-top: 1.5em;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        input[type="submit"]:hover {
            background-color: #8a2be2;
        }
        .floating-element {
            position: absolute;
            opacity: 0.7;
            pointer-events: none;
            animation: float 20s infinite ease-in-out;
        }
        @keyframes float {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            25% { transform: translate(20px, -20px) rotate(5deg); }
            50% { transform: translate(-10px, 15px) rotate(-5deg); }
            75% { transform: translate(15px, 10px) rotate(3deg); }
        }
        .mist {
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(ellipse at center, 
                rgba(255,255,255,0.2) 0%,
                rgba(255,255,255,0.1) 50%,
                rgba(255,255,255,0) 70%);
            animation: mistMove 30s linear infinite;
            pointer-events: none;
            z-index: 1;
            mix-blend-mode: overlay;
        }
        @keyframes mistMove {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(50%, 50%) rotate(360deg); }
        }
        .sparkle {
            position: absolute;
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background-color: white;
            opacity: 0;
            pointer-events: none;
            animation: sparkle 4s infinite;
            z-index: 3;
        }
        @keyframes sparkle {
            0%, 100% { opacity: 0; transform: scale(0) translate(0, 0); }
            50% { opacity: 1; transform: scale(1) translate(10px, -10px); }
        }

        .error {
            color: red;
        }
        
    </style>
</head>
<body>
    <div class="container">
        <div class="mist"></div>
        <div class="mist" style="animation-delay: -15s;"></div>
        
        <svg class="floating-element" style="top: 10%; left: 10%;" width="100" height="100" viewBox="0 0 100 100">
            <path d="M10,50 Q50,10 90,50 T10,50" fill="none" stroke="#FF69B4" stroke-width="3"/>
            <circle cx="50" cy="50" r="20" fill="#87CEFA" opacity="0.7"/>
        </svg>
        
        <svg class="floating-element" style="top: 70%; left: 80%;" width="120" height="120" viewBox="0 0 120 120">
            <polygon points="60,10 100,40 80,90 40,90 20,40" fill="#DDA0DD" opacity="0.8"/>
            <circle cx="60" cy="60" r="30" fill="none" stroke="#4B0082" stroke-width="3"/>
        </svg>
        
        <svg class="floating-element" style="top: 40%; left: 5%;" width="80" height="80" viewBox="0 0 80 80">
            <rect x="10" y="10" width="60" height="60" fill="#98FB98" opacity="0.6" transform="rotate(45 40 40)"/>
            <circle cx="40" cy="40" r="25" fill="none" stroke="#FFD700" stroke-width="3"/>
        </svg>
        
        <svg class="floating-element" style="top: 20%; right: 10%;" width="140" height="140" viewBox="0 0 140 140">
            <path d="M70,20 Q90,60 70,100 T70,20" fill="#FFA07A" opacity="0.7"/>
            <ellipse cx="70" cy="70" rx="40" ry="30" fill="none" stroke="#8A2BE2" stroke-width="3"/>
        </svg>
        

        <!-- Formulari -->
        <div class="form-container">
            <h2>Formulari</h2>
            <form action="validacio.php" method="post">
                <label for="nom">Nom:</label>
                <input type="text" id="nom" name="nom">

                <!-- Mostrem l'error en cas que hi hagi -->
                <span class="error"><?= isset($errors['nom']) ? $errors['nom'] : ""; ?></span>

                <label for="password">Contrasenya:</label>
                <input type="password" id="password" name="password">
                <span class="error"><?= isset($errors['password']) ? $errors['password'] : ""; ?></span>

                <label for="formacio">Formació:</label>
                <select id="formacio" name="formacio">
                    <option value="">Selecciona una opció</option>
                    <option value="ESO">ESO</option>
                    <option value="FP">FP</option>
                    <option value="BAT">BAT</option>
                </select>

                <label>Idiomes:</label>
                <div>
                    <label><input type="checkbox" name="idiomes[]" value="catala"> Català</label>
                    <label><input type="checkbox" name="idiomes[]" value="castella"> Castellà</label>
                    <label><input type="checkbox" name="idiomes[]" value="angles"> Anglès</label>
                    <label><input type="checkbox" name="idiomes[]" value="frances"> Francés</label>
                    <label><input type="checkbox" name="idiomes[]" value="alemany"> Alemany</label>
                </div>
                <span class="error"><?= isset($errors['idiomes']) ? $errors['idiomes'] : ""; ?></span>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email">
                <span class="error"><?= isset($errors['email']) ? $errors['email'] : ""; ?></span>

                <label for="web">Lloc web:</label>
                <input type="text" id="web" name="web">
                <span class="error"><?= isset($errors['web']) ? $errors['web'] : ""; ?></span>

                <input type="submit" value="Enviar">
            </form>
        </div>
    </div>

    <!-- Aspectes visuals -->
    <script>
        function createSparkles() {
            const container = document.querySelector('.container');
            for (let i = 0; i < 50; i++) {
                const sparkle = document.createElement('div');
                sparkle.classList.add('sparkle');
                sparkle.style.left = `${Math.random() * 100}%`;
                sparkle.style.top = `${Math.random() * 100}%`;
                sparkle.style.animationDelay = `${Math.random() * 4}s`;
                container.appendChild(sparkle);
            }
        }
        
        function animateFloatingElements() {
            const elements = document.querySelectorAll('.floating-element');
            elements.forEach(el => {
                el.style.animationDuration = `${20 + Math.random() * 10}s`;
                el.style.animationDelay = `${Math.random() * -20}s`;
            });
        }
        
        createSparkles();
        animateFloatingElements();
    </script>
</body>
</html>