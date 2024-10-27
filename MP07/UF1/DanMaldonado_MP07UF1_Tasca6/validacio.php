<?php
session_start();

// Comprovem que s'ha arrivat a la página mitjançant el sumbit
if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    // Netejem les dades
    function cleanData($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }

    function validar_contrasenya($password) {
        // Comprovar que la contrasenya compleixi amb tots els requisits
        return !empty($password) &&
                preg_match('/[A-Z]/', $password) &&  // Almenys una majúscula
                preg_match('/[a-z]/', $password) &&  // Almenys una minúscula
                preg_match('/[0-9]/', $password) &&  // Almenys un número
                preg_match('/[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]+/', $password) &&  // Almenys un caràcter especial
                strlen($password) >= 8;  // Mínim de 8 caràcters
    }

    $_SESSION['errors'] = []; // Inicialitzem el array d'errors

    // Inicialitzem variables
    $nom = cleanData($_POST['nom']);
    $password = cleanData($_POST['password']);
    $formacio = $_POST['formacio'];
    $idiomes = $_POST['idiomes'];
    $email = cleanData($_POST['email']);
    $web = cleanData($_POST['web']);

    // Validar nom
    if (empty($nom) || !preg_match('/^[a-zA-Z ]+$/', $nom)) {
        $_SESSION['errors']['nom'] = "* El nom ha de contenir només lletres i espais.";
    }

    // Validar contrasenya
    if (!filter_var($password, FILTER_CALLBACK, ['options' => 'validar_contrasenya'])) {
        $_SESSION['errors']['password'] = "* La contrasenya ha de tenir almenys 8 caràcters, incloent 1 majúscula, 1 minúscula, 1 xifra i 1 caràcter especial.";
    }

    if (empty($idiomes) || count($idiomes) != 1) {
        $_SESSION['errors']['idiomes'] = "* Seleccioneu només 1 opció.";
    }

    // Validar email
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['errors']['email'] = "* L'email no és vàlid.";
    }

    // Validar URL
    if (!empty($web)) {
        if (!filter_var($web, FILTER_VALIDATE_URL)) {
            $_SESSION['errors']['web'] = "* L'URL no és vàlida.";
        }
    }
}

// Tornem al index
header("Location: index.php");
exit;
?>