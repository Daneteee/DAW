<?php
session_start();
include 'config/db.php';

// Verificar si el usuario está autenticado
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

// Obtener los datos enviados desde el formulario
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $entrada_id = $_POST['id'];
    $titol = trim($_POST['titol']);
    $descripcio = trim($_POST['descripcio']);
    $categoria_id = $_POST['categoria_id'];

    // Verificar que el usuario sea el autor de la entrada
    $query_verificar = "SELECT usuari_id FROM entrades WHERE id = ?";
    $stmt = $db->prepare($query_verificar);
    $stmt->bind_param("i", $entrada_id);
    $stmt->execute();
    $result = $stmt->get_result();
    $entrada = $result->fetch_assoc();

    if (!$entrada || $entrada['usuari_id'] != $_SESSION['user_id']) {
        $_SESSION['message'] = [
            'type' => 'error',
            'text' => 'No tens permisos per editar aquesta entrada.'
        ];
        header("Location: index.php");
        exit();
    }

    // Actualizar la entrada
    $stmt = $db->prepare("UPDATE entrades SET titol = ?, descripcio = ?, categoria_id = ? WHERE id = ?");
    $stmt->bind_param("ssii", $titol, $descripcio, $categoria_id, $entrada_id);

    if ($stmt->execute()) {
        $_SESSION['message'] = [
            'type' => 'success',
            'text' => 'Entrada actualitzada correctament.'
        ];
    } else {
        $_SESSION['message'] = [
            'type' => 'error',
            'text' => 'Error en actualitzar l\'entrada.'
        ];
    }

    header("Location: index.php");
    exit();
}
?>
