<?php include "includes/header.php"; ?>
<?php 
if (!isset($_SESSION)) {
    session_start();
}
?>

<div class="main-content container">
    <h1 class="page-title">Entrades del Blog</h1>
    <?php
    include 'config/db.php'; 

    // Agafem les entrades
    $query = "SELECT e.id, e.titol, e.descripcio, e.data, u.nom AS usuari_nom, c.nombre AS categoria_nombre
            FROM entrades e
            INNER JOIN usuaris u ON e.usuari_id = u.id
            INNER JOIN categories c ON e.categoria_id = c.id
            ORDER BY e.data DESC";

    $result = $db->query($query);

    if ($result->num_rows > 0) {

        // Mostrem les entrades
        while ($entrada = $result->fetch_assoc()) {
            ?>
            <div class="blog-entry">
                <div class="blog-entry-header">
                    <h2 class="blog-entry-title"><?php echo htmlspecialchars($entrada['titol']); ?></h2>
                    <div class="blog-entry-meta">
                        <span class="meta-info">
                            <i class="icon-category"></i> <?php echo htmlspecialchars($entrada['categoria_nombre']); ?> | 
                            <i class="icon-user"></i> <?php echo htmlspecialchars($entrada['usuari_nom']); ?> | 
                            <i class="icon-calendar"></i> <?php echo date('d/m/Y', strtotime($entrada['data'])); ?>
                        </span>
                        <?php 
                        if (isset($_SESSION['user_id'])) {
                            $query_autor = "SELECT usuari_id FROM entrades WHERE id = " . $entrada['id'];
                            $result_autor = $db->query($query_autor);
                            $autor = $result_autor->fetch_assoc();
                            
                            // Comprovem que només l'autor pugui eliminar o editar entrades
                            if ($autor['usuari_id'] == $_SESSION['user_id']) {
                                ?>

                                <!-- Butons per editar o eliminar entrada -->
                                <div class="entry-actions">
                                    <a href="edit_entry.php?id=<?php echo $entrada['id']; ?>" class="btn btn-edit">
                                        <i class="icon-edit"></i> Editar
                                    </a>
                                    <a href="delete_entry.php?id=<?php echo $entrada['id']; ?>" 
                                       class="btn btn-delete" 
                                       onclick="return confirm('Estàs segur que vols eliminar aquesta entrada?')">
                                       <i class="icon-delete"></i> Eliminar
                                    </a>
                                </div>
                                <?php
                            }
                        }
                        ?>
                    </div>
                </div>

                <!-- Descripció de l'entrada -->
                <div class="blog-entry-body">
                    <p class="card-text" style="overflow: hidden; text-overflow: ellipsis;">
                    <?php echo nl2br(htmlspecialchars($entrada['descripcio'])); ?>
                    </p>
                </div>
            </div>
            <?php
        }
    } else {
        echo "<div class='no-entries'>Encara no hi han entrades.</div>"; 
    }

    $db->close();
    ?>
</div>

<?php include 'includes/sidebar.php'; ?>
<?php include "includes/footer.php"; ?>
