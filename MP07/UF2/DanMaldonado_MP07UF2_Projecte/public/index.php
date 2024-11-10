<?php include "includes/header.php"; ?>

<div class="main-content">
    <?php
    include 'db_connection.php'; 

    // Agafem les entrades
    $query = "SELECT e.titol, e.descripcio, e.data, u.nom AS usuari_nom, c.nombre AS categoria_nombre
            FROM entrades e
            INNER JOIN usuaris u ON e.usuari_id = u.id
            INNER JOIN categories c ON e.categoria_id = c.id
            ORDER BY e.data DESC";

    $result = $db->query($query);

    // Verifiquem si hi han entrades i en cas que hi hagin les mostrem
    if ($result->num_rows > 0) {
        // 
    } else {
        echo "<p>Encara no hi han entrades.</p>"; 
    }

    $db->close();
    ?>
</div>

<?php include 'includes/sidebar.php'; ?>
<?php include "includes/footer.php"; ?>
