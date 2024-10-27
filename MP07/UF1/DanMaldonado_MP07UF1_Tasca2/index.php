<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="get" action="Ex1.php">
        <h1>Cálcul d'àrea</h1>
        <label for="length">Alçada  :</label>
        <input type="text" id="length" name="length" >
        <br>
        <label for="width">Amplada:</label>
        <input type="text" id="width" name="width" >
        <br>
        <input type="submit" value="Calcular Àrea">
        <br>
        <br>
    </form>    

    <form method="get" action="Ex2.php">
    <h1>Díes dels mesos</h1>
        <label for="mes">Mes:</label>
        <input type="text" id="mes" name="mes" >
        <br>
        <input type="submit" value="Info del mes">
    </form>
    
    <form method="get" action="Ex3.php">
        <br>
        <br>
        <h1>Conversor de Temperatura</h1>
        <p>De:</p>
        <label>
            <input type="radio" name="convertir_de" value="fahrenheit"> Fahrenheit
            <input type="radio" name="convertir_de" value="celsius"> Celsius
            <input type="radio" name="convertir_de" value="kelvin"> Kelvin
        </label>
        <br>
        <input type="text" id="temp" name="temp">
        <p>A:</p>
        <label>
            <input type="radio" name="convertir_a" value="fahrenheit"> Fahrenheit
            <input type="radio" name="convertir_a" value="celsius"> Celsius
            <input type="radio" name="convertir_a" value="kelvin"> Kelvin
        </label>
        <br>   
        <br>   
        <input type="submit" value="Convertir">
    </form>

    <form method="post" action="Ex4.php">
        <br>   
        <br>   
        <h1>Validador de contrasenya</h1>
        <label for="contrasenya">Contrasenya:</label>
        <input type="text" id="contrasenya" name="contrasenya" >
        <br>
        <input type="submit" value="Validar">
    </form>

    <form method="get" action="Ex5.php">
        <br>   
        <br>   
        <h1>Filtrar array</h1>
        <label for="filtre">Llista de nombres (separat per comes):</label>
        <input type="text" id="filtre" name="filtre" >
        <br>
        <input type="submit" value="Enviar">
    </form>

</body>
</html>
