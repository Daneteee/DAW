<?php
session_start();
require_once 'config/db.php';

// Verificar si el usuario está autenticado
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

// Obtener ID de la entrada
$entrada_id = $_GET['id'] ?? null;

// Verificar que el usuario sea el autor
$query_verificar = "SELECT usuari_id FROM entrades WHERE id = ?";
$stmt = $db->prepare($query_verificar);
$stmt->bind_param("i", $entrada_id);
$stmt->execute();
$result = $stmt->get_result();
$entrada = $result->fetch_assoc();

if (!$entrada || $entrada['usuari_id'] != $_SESSION['user_id']) {
    $_SESSION['message'] = [
        'type' => 'error',
        'text' => 'No tens permisos per editar aquesta entrada.'
    ];
    header("Location: index.php");
    exit();
}

// Cargar entrada para edición
$query_entry = "SELECT * FROM entrades WHERE id = ?";
$stmt = $db->prepare($query_entry);
$stmt->bind_param("i", $entrada_id);
$stmt->execute();
$result = $stmt->get_result();
$entrada = $result->fetch_assoc();

// Obtener categorías
$categories_query = "SELECT * FROM categories ORDER BY nombre";
$categories_result = $db->query($categories_query);
$categories = [];
if ($categories_result) {
    while ($row = $categories_result->fetch_assoc()) {
        $categories[] = $row;
    }
}
?>

<?php include "includes/header.php"; ?>

<?php if (!empty($categories)): ?>
<div class="categories-bar">
    <ul>
        <?php foreach ($categories as $category): ?>
            <li><a href="category.php?name=<?= urlencode($category['nombre']) ?>"><?= htmlspecialchars($category['nombre']) ?></a></li>
        <?php endforeach; ?>
    </ul>
</div>
<?php endif; ?>

<main class="main-content">
    <div class="category-form-container">
        <h2>Editar Entrada</h2>
        
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
        
        <form action="process_edit_entry.php" method="POST" class="elegant-form">
            <input type="hidden" name="id" value="<?= $entrada_id ?>">
            <div class="form-group">
                <label for="titol">
                    <i class="ri-text"></i> Títol de l'Entrada
                </label>
                <div class="input-wrapper">
                    <input type="text" id="titol" name="titol" 
                           value="<?= htmlspecialchars($entrada['titol']) ?>" 
                           placeholder="Escriu el títol de l'entrada" 
                           required 
                           minlength="2" 
                           maxlength="100">
                    <span class="input-icon"></span>
                </div>
            </div>

            <div class="form-group">
                <label for="descripcio">
                    <i class="ri-edit-line"></i> Descripció
                </label>
                <div class="input-wrapper">
                    <textarea id="descripcio" name="descripcio" 
                              placeholder="Escriu el contingut de l'entrada" 
                              required 
                              minlength="10" 
                              maxlength="5000" 
                              rows="5"
                              style="resize: none; width: 300px;"><?= htmlspecialchars($entrada['descripcio']) ?></textarea>
                </div>
            </div>

            <div class="form-group">
                <label for="categoria_id">
                    <i class="ri-folder-line"></i> Categoria
                </label>
                <div class="input-wrapper">
                    <select id="categoria_id" name="categoria_id" required>
                        <option value="">Selecciona una categoria</option>
                        <?php foreach ($categories as $category): ?>
                            <option value="<?= $category['id'] ?>" 
                                <?= $category['id'] == $entrada['categoria_id'] ? 'selected' : '' ?>>
                                <?= htmlspecialchars($category['nombre']) ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </div>
            
            <button type="submit" class="submit-btn">
                <i class="ri-add-circle-line"></i> Actualitzar Entrada
            </button>
        </form>
    </div>
</main>

<?php include 'includes/sidebar.php'; ?>
<?php include "includes/footer.php"; ?>
