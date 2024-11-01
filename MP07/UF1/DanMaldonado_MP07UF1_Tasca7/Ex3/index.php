<?php
// Verificar si 'dades.csv' está vacío
if (!file_exists('dades.csv') || filesize('dades.csv') == 0) {
    require 'generar_dades.php';
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Registre d'usuaris</title>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
        }
        button {
            background-color: purple;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: teal;
        }
    </style>
</head>
<body>
    <h2>Registre d'usuaris</h2>
    <form action="processa.php" method="get">
        <div class="form-group">
            <label for="nom">Nom:</label>
            <input type="text" id="nom" name="nom" required>
        </div>
        <div class="form-group">
            <label for="cognom">Cognom:</label>
            <input type="text" id="cognom" name="cognom" required>
        </div>
        <div class="form-group">
            <label for="data_naixement">Data de naixement:</label>
            <input type="date" id="data_naixement" name="data_naixement" required>
        </div>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>