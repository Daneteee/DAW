<?php
session_start(); 
include 'db_connection.php';

// Array d'errors
if (!isset($_SESSION['errors'])) {
    $_SESSION['errors'] = [];
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $query = "SELECT * FROM usuaris WHERE email = ?";
    $stmt = $db->prepare($query);

    if (!$stmt) {
        die("Error en la preparació: " . $db->error);
    }

    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    // Verifiquem la contrasenya
    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        if (password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['user_name'] = $user['nom'];


            $_SESSION['errors'] = []; 
        } else {
            $_SESSION['errors']['login'] = "*Credencials incorrectes.";
        }
    } else {
        $_SESSION['errors']['login'] = "*Credencials incorrectes.";
    }

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

        <!-- Enviem el formulari a la mateixa pàgina -->
        <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
            <label for="email">Email: </label>
            <input type="email" name="email" required>
            <label for="password">Contraseña: </label>
            <input type="password" name="password" required>
            <input type="submit" value="Iniciar sessió">
        </form>
    <?php else: ?>
        <p>Ja estás loguejat com a <?php echo $_SESSION['user_name']; ?>. 
        <a href="logout.php">Cerrar sesión</a></p>
    <?php endif; ?>

    <!-- Mostrem errors si n'hi ha -->
    <?php if (!empty($_SESSION['errors']['login'])): ?>
        <p style="color:red;"><?php echo $_SESSION['errors']['login']; ?></p>
    <?php endif; ?>

    <?php
    unset($_SESSION['errors']);
    ?>
</body>
</html>
