<?php
# index.php la primera on l’usuari és logueja (email, i password). Si l’usuari ja està loguejat, no mostraràs el formulari, 
# sinó redirigeix a benvinguda.php. (La sessió ha de ser d’1 minut)


session_start();

# Si no està loguejat, mostrem el formulari
if (!isset($_SESSION['email'])) {
    if (isset($_SESSION["missatge"])) {
        echo "<p>" . $_SESSION["missatge"] . "</p>";
    }

    echo '
    <h1>Inicia sessió</h1>
    <form method="post" action="benvinguda.php">
        <label for="email">Correu electrònic:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <br>
        <label for="password">Contrasenya:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <br>
        <button type="submit">Iniciar sessió</button>
    </form>';
} else {
    # Si está loguejat eniem a benvinguda.php
    header("Location: benvinguda.php");
    exit;
}
?>
