<?php

# benvinguda.php La segona en cas que l’usuari s’hagi loguejat correctament (qualsevol email amb el domini @lacetania.cat, i password 1234) 
# digui benvingut, i mostri el botó de logout. Si l’usuari intenta accedir  a benvinguda.php sense està loguejat l’envia a index.php i 
# apareix el missatge, On vas? primer t’has de loguejar. Si s’equivoca en les dades d’identificació que redirigeixi a index.php i 
# aparegui el missatge: “credencials no vàlides”

session_start();

# Comprovem que la sessió no estigui iniciada
if (!isset($_SESSION['email'])) {

    # Comprovem que s'han enviat les dades del formulari
    if (isset($_POST['email']) && isset($_POST['password'])) {
        $email = $_POST['email'];
        $password = $_POST['password'];
    
        # Comprovem que siguin correctes
        if (strpos($email, '@lacetania.cat') !== false && $password == '1234') {
            $_SESSION['email'] = $email;

        } else {
            # Si no són correctes, tornem a la pàgina d'inici de sessió amb un missatge d'error
            session_unset();
            $_SESSION['missatge'] = "Credencials no valides";
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
if (isset($_SESSION['email'])) {

    # Si está iniciada comprovem que no s'ha exedit el temps d'inactivitat
    $seg_inactivitat = 60;
    if (isset($_SESSION["timeout"])) {
        $sessionTTL = time() - $_SESSION["timeout"];
        if ($sessionTTL > $seg_inactivitat) {
            header("Location: logout.php");
            exit;
        }
    }
    $_SESSION["timeout"] = time();

    echo "<h1>Benvingut, " . htmlspecialchars($_SESSION['email']) . "!</h1>";
    echo "<button><a href='logout.php'>Logout</a></button>";
}
?>
