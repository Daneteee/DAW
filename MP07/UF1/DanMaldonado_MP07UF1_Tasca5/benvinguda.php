<?php

# benvinguda.php La segona en cas que l’usuari s’hagi loguejat correctament (qualsevol user amb el domini @lacetania.cat, i password 1234) 
# digui benvingut, i mostri el botó de logout. Si l’usuari intenta accedir  a benvinguda.php sense està loguejat l’envia a index.php i 
# apareix el missatge, On vas? primer t’has de loguejar. Si s’equivoca en les dades d’identificació que redirigeixi a index.php i 
# aparegui el missatge: “credencials no vàlides”

session_start();

# Comprovem que la sessió no estigui iniciada
if (!isset($_SESSION['user'])) {

    # Comprovem que s'han enviat les dades del formulari
    if (isset($_POST['user']) && isset($_POST['password'])) {
        $user = $_POST['user'];
        $password = $_POST['password'];
        
        # Defineix un array d'usuaris autoritzats
        $validUsers = [
            'vot1' => '1234',
            'vot2' => '5678'
        ];

        # Comprovem que l'user estigui en l'array i que la contrasenya sigui correcta
        if (isset($validUsers[$user]) && $validUsers[$user] === $password) {
            $_SESSION['user'] = $user;
        } else {
            # Si no són correctes, tornem a la pàgina d'inici de sessió amb un missatge d'error
            session_unset();
            $_SESSION['missatge'] = "Credencials no vàlides";
            header("Location: index.php");
            exit;
        } 
    } else {
        # Si s'ha intentat accedir sense enviar dades, tornem a la pàgina d'inici de sessió amb un missatge d'error
        session_unset();
        $_SESSION['missatge'] = "On vas? Primer t'has de loguejar";
        header("Location: index.php");
        exit;
    }
}

# Comprovem que la sessió estigui iniciada
if (isset($_SESSION['user'])) {

    # Si està iniciada comprovem que no s'ha excedit el temps d'inactivitat
    $seg_inactivitat = 3600;
    if (isset($_SESSION["timeout"])) {
        $sessionTTL = time() - $_SESSION["timeout"];
        if ($sessionTTL > $seg_inactivitat) {
            header("Location: logout.php");
            exit;
        }
    }
    $_SESSION["timeout"] = time();

    echo "<h1>Benvingut, " . htmlspecialchars($_SESSION['user']) . "!</h1>";
    echo "<form method='post' action='processavot.php'>
        <label for='vot'>Vota:</label><br>
        <input type='radio' id='si' name='vot' value='si'>
        <label for='si'>Sí</label><br>
        <input type='radio' id='no' name='vot' value='no'>
        <label for='no'>No</label><br>
        <input type='radio' id='blanc' name='vot' value='blanc'>
        <label for='blanc'>Blanc</label><br>
        <input type='submit' value='Enviar'>
    </form>";
}
?>
