<aside>
    <h2>Menú</h2>
    <ul>
        <?php if (!isset($_SESSION['user_id'])):?>
            <li>
                <h3>Iniciar Sesión</h3>

                <?php if (!empty($_SESSION['errors']['login'])): ?>
                    <p style="color:red;"><?php echo $_SESSION['errors']['login']; ?></p>
                    <?php unset($_SESSION['errors']['login']);?>
                <?php endif; ?>
                
                <form action="login.php" method="POST">
                    <label for="email">Email:</label>
                    <input type="email" name="email" required>
                    <label for="password">Contraseña:</label>
                    <input type="password" name="password" required>
                    <input type="submit" value="Iniciar sesión">
                </form>
            </li> 
            <li>
                <br><br>
                <h3>Registrar Usuario</h3>
                <?php include 'register.php'; ?>
            </li>
        <?php else: ?>
            <li><a href="create_category.php">Crear categoría</a></li>
            <li><a href="create_entry.php">Crear entrada</a></li>
            <li><a href="logout.php">Cerrar sesión</a></li>
        <?php endif; ?>
    </ul>
</aside>
