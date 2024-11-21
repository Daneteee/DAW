<?php
session_start(); // Asegúrate de iniciar la sesión al principio
include 'db_connection.php';

// Inicializamos el array de errores si no existe
if (!isset($_SESSION['errors'])) {
    $_SESSION['errors'] = [];
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $query = "SELECT * FROM usuaris WHERE email = ?";
    $stmt = $db->prepare($query);

    if (!$stmt) {
        die("Error en la preparación de la consulta: " . $db->error);
    }

    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        if (password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['user_name'] = $user['nom'];

            // No hacemos la redirección aquí, sino en el archivo de login
            $_SESSION['errors'] = []; // Limpiamos los errores antes de redirigir
        } else {
            // Credenciales incorrectas
            $_SESSION['errors']['login'] = "*Credencials incorrectes.";
        }
    } else {
        // Usuario no encontrado
        $_SESSION['errors']['login'] = "*Credencials incorrectes.";
    }

    // Redirigimos después de establecer los errores en la sesión
    header("Location: index.php");
    exit;

    $stmt->close();
    $db->close();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <?php if (!isset($_SESSION['user_id'])): ?>
        <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
            <label for="email">Email: </label>
            <input type="email" name="email" required>
            <label for="password">Contraseña: </label>
            <input type="password" name="password" required>
            <input type="submit" value="Iniciar sesión">
        </form>
    <?php else: ?>
        <p>Ya estás logueado como <?php echo $_SESSION['user_name']; ?>. 
        <a href="logout.php">Cerrar sesión</a></p>
    <?php endif; ?>

    <!-- Mostramos el error si existe -->
    <?php if (!empty($_SESSION['errors']['login'])): ?>
        <p style="color:red;"><?php echo $_SESSION['errors']['login']; ?></p>
    <?php endif; ?>

    <?php
    // Limpiamos los errores después de mostrarlos
    unset($_SESSION['errors']);
    ?>
</body>
</html>
