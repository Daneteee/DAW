<aside>
    <h2>Menú</h2>
    <ul>
        <!-- Verificar si el usuario está logueado -->
        <?php if (!isset($_SESSION['user_id'])): ?>
            <!-- Si el usuario no ha iniciado sesión, mostrar los formularios de login y registro -->
            <!-- <li><h3>Iniciar Sesión</h3>
            <?php //include 'login.php'; // Incluir el formulario de login ?>
            </li> -->
            <li><h3>Registrar Usuario</h3>
            <?php include 'register.php'; // Incluir el formulario de registro ?>
            </li>
        <?php else: ?>
            <!-- Si el usuario ha iniciado sesión, mostrar la opción para cerrar sesión -->
            <li><a href="logout.php">Cerrar sesión</a></li>
        <?php endif; ?>
    </ul>
</aside>
