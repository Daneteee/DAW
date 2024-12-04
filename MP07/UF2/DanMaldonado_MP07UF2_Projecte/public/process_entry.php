<?php
session_start();
require_once 'config/db.php'; 

function validateEntry($titol, $contingut, $categoria_id, $db) {
    if (empty($titol)) {
        return "El títol de l'entrada no pot estar buit.";
    }

    if (!preg_match('/^[a-zA-ZàèìòùáéíóúñçÀÈÌÒÙÁÉÍÓÚÑÇ\s]+$/', $titol)) {
        return "El títol només pot contenir lletres.";
    }

    if (empty($contingut)) {
        return "El contingut de l'entrada no pot estar buit.";
    }

    if ($categoria_id === null || $categoria_id === '') {
        return "Cal seleccionar una categoria.";
    }

    $stmt = $db->prepare("SELECT COUNT(*) as count FROM entrades WHERE LOWER(titol) = LOWER(?)");
    $stmt->bind_param("s", $titol);
    $stmt->execute();
    $result = $stmt->get_result();
    $row = $result->fetch_assoc();
    $stmt->close();

    if ($row['count'] > 0) {
        return "Ja existeix una entrada amb aquest títol.";
    }

    return null;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Verificar si el usuario está autenticado
    if (!isset($_SESSION['user_id'])) {
        header("Location: login.php");
        exit();
    }

    $titol = trim($_POST['titol']);
    $contingut = trim($_POST['contingut']);
    $categoria_id = $_POST['categoria_id'] ?? null;
    $usuari_id = $_SESSION['user_id'];

    $error = validateEntry($titol, $contingut, $categoria_id, $db);

    if ($error === null) {
        // Agregar el usuari_id a la consulta de inserción
        $stmt = $db->prepare("INSERT INTO entrades (titol, descripcio, categoria_id, usuari_id, data) VALUES (?, ?, ?, ?, NOW())");
        $stmt->bind_param("ssii", $titol, $contingut, $categoria_id, $usuari_id);

        try {
            if ($stmt->execute()) {
                $_SESSION['message'] = [
                    'type' => 'success',
                    'text' => "L'entrada '{$titol}' s'ha creat amb èxit!"
                ];
            } else {
                $_SESSION['message'] = [
                    'type' => 'error',
                    'text' => "Error en crear l'entrada: " . $db->error
                ];
            }
            $stmt->close();
        } catch (Exception $e) {
            $_SESSION['message'] = [
                'type' => 'error', 
                'text' => "S'ha produït un error inesperat: " . $e->getMessage()
            ];
        }
    } else {
        $_SESSION['message'] = [
            'type' => 'warning',
            'text' => $error
        ];
    }

    header("Location: create_entry.php");
    exit;
} else {
    header("Location: create_entry.php");
    exit;
}