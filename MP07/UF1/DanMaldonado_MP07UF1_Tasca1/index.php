<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulari de Nom d'Usuari</title>
</head>
<body>

    <!-- 1. Creeu un formulari HTML senzill i accepteu el nom d'usuari i 
    visualitzeu-lo mitjançant la declaració d'echo PHP. --> 

    <h1>Introduïu el vostre nom d'usuari</h1>
        
        <!-- Creem el formulari-->
    <form method="get" action="">
        <input type="text" id="nom" name="nom" required>
        <input type="submit" value="Enviar">
    </form>

    <?php 
    // Comprovem si s'ha enviat el formulari
    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        // Obtenim el nom d'usuari del formulari i el mostrem
        $nom = htmlspecialchars($_GET['nom']);
        echo "<h2>Hola, $nom!</h2>";
    }

    
    // 2. Escriu un script php que donades 3 variables s1,s2 i s3, que corresponent als sou de 3 treballadors 
    # els mostri en una taula.
    
    $s1 = 1000; 
    $s2 = 1200; 
    $s3 = 1400; 
    echo "<br>";
    echo "<table border='1' cellspacing='0' cellpadding='5'>";
    echo "<tr><td style='color: blue;'>Salary of Mr.A is</td><td>" . number_format($s1, 2) . " €</td></tr>";
    echo "<tr><td style='color: blue;'>Salary of Mr.B is</td><td>" . number_format($s2, 2) . " €</td></tr>";
    echo "<tr><td style='color: blue;'>Salary of Mr.C is</td><td>" . number_format($s3, 2) . " €</td></tr>";
    echo "</table>";

    
    // 3. Escriu un programa PHP per comprovar si un nombre és un nombre Armstrong o no. 
    # Mostra el missatge el nombre xxx  (no) és Armstrong.
    
    function armstrong_number($num) {
        $numStr = (string)$num;
        $suma = 0;

        # Per cada digit fem el cub i el sumem a la variable
        for ($i = 0; $i < strlen($numStr); $i++) {
            $suma += (int)$numStr[$i]**3;

        }
        # Creem els condicionals corresponents
        if ($suma == $num) {
            return "SI és un nombre Armstrong.";
        } else {
            return "NO és un nombre Armstrong.";
        }
    }
    echo "<br>";
    echo "Is 153 Armstrong number " . armstrong_number(153) . "<br>";
    echo "\nIs 153 Armstrong number " . armstrong_number(21) . "<br>";
    echo "\nIs 153 Armstrong number " . armstrong_number(4587) . "<br>";


    // 4. Escriu un programa en php utilitzant 2 bucles for aniuats que imprimeixi pel navegador un taules d’escacs
    echo "<br><br>";    
    $num = 0;
    $color = "white";

    echo '<table border="1" cellspacing="0" cellpadding="0" width="400px" height="400px">';

    # Creem el primer bucle per les files
    for ($i = 0; $i < 8; $i++) {
        echo '<tr>';
        
        # Creem el segon bucle per les columnes
        for ($j = 0; $j < 8; $j++) {

            # Depenent si es parell o senar canviem el color
            if (($i + $j) % 2 == 0) {
                $color = "white";
            } else {
                $color = "black";
            }
            
            echo '<td style="background-color: ' . $color . ';"></td>';
        }
        
        echo '</tr>';
    }

    echo '</table>';
    ?>

    

</body>
</html>
