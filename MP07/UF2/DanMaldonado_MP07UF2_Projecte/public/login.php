<?php

// include 'db_connection.php';

// $error_message = ''; // Para almacenar el mensaje de error si es necesario

// if ($_SERVER["REQUEST_METHOD"] == "POST") {
//     $email = $_POST['email'];
//     $password = $_POST['password'];

//     $query = "SELECT * FROM usuaris WHERE email = ?";
//     $stmt = $db->prepare($query);

//     if (!$stmt) {
//         die("Error en la preparación de la consulta: " . $db->error);
//     }

//     $stmt->bind_param("s", $email);
//     $stmt->execute();
//     $result = $stmt->get_result();

//     if ($result->num_rows > 0) {
//         $user = $result->fetch_assoc();
//         if (password_verify($password, $user['password'])) {
//             $_SESSION['user_id'] = $user['id'];
//             $_SESSION['user_name'] = $user['nom'];

//             header("Location: index.php"); // Redirigir después de iniciar sesión
//             exit;
//         } else {
//             $error_message = "Contraseña incorrecta";
//         }
//     } else {
//         $error_message = "Usuario no encontrado";
//     }

//     $stmt->close();
//     $db->close();
// }
?>

<!-- Formulario de login -->
<?php if (!isset($_SESSION['user_id'])): ?>
    <!-- <form action="index.php" method="POST">
        <label for="email">Email: </label><input type="email" name="email" required>
        <label for="password">Contraseña: </label><input type="password" name="password" required>
        <input type="submit" value="Iniciar sesión">
    </form> -->
<?php else: ?>
    <!-- <p>Ya estás logueado como <?php echo $_SESSION['user_name']; ?>. <a href="logout.php">Cerrar sesión</a></p> -->
<?php endif; ?>

<?php
// if (isset($error_message)) {
//     echo "<p style='color:red;'>$error_message</p>";
// }
?>
