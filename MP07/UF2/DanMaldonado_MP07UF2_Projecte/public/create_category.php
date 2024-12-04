<?php
if (!isset($_SESSION)) {
    session_start();
}
?>

<?php include "includes/header.php"; ?>

<main class="main-content">
    <div class="category-form-container">
        <h2>Crear Nova Categoria</h2>
        
        <?php 
        if (isset($_SESSION['message'])) {
            $message = $_SESSION['message'];
            $iconClass = match($message['type']) {
                'success' => 'ri-checkbox-circle-line text-green',
                'error' => 'ri-close-circle-line text-red',
                'warning' => 'ri-warning-line text-orange',
                default => ''
            };
            ?>
            <div class="notification <?= $message['type'] ?>">
                <i class="<?= $iconClass ?> notification-icon"></i>
                <span><?= htmlspecialchars($message['text']) ?></span>
            </div>
            <?php 
            unset($_SESSION['message']); 
        } 
        ?>
        
        <form action="process_category.php" method="POST" class="elegant-form">
            <div class="form-group">
                <label for="nom_categoria">
                    <i class="ri-price-tag-3-line"></i> Nom de la Categoria
                </label>
                <div class="input-wrapper">
                    <input type="text" id="nom_categoria" name="nom_categoria" 
                           placeholder="Escriu el nom de la categoria" 
                           required 
                           minlength="2" 
                           maxlength="50">
                </div>
            </div>
            
            <button type="submit" class="submit-btn">
                <i class="ri-add-circle-line"></i> Crear Categoria
            </button>
        </form>
    </div>
</main>

<?php include 'includes/sidebar.php'; ?>
<?php include "includes/footer.php"; ?>