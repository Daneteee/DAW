<?php

// Función para listar las categorías desde la base de datos
function llistarCategories($db) {
    // Definimos la consulta para obtener todas las categorías ordenadas por id
    $query = "SELECT id, nombre FROM categories ORDER BY id ASC";

    // Ejecutamos la consulta
    $result = $db->query($query);

    // Comprobamos si la consulta fue exitosa y si hay resultados
    if ($result && $result->num_rows > 0) {
        // Creamos un array para almacenar las categorías
        $categories = [];
        
        // Iteramos sobre los resultados y los añadimos al array
        while ($category = $result->fetch_assoc()) {
            $categories[] = $category;
        }

        // Devolvemos el array con las categorías
        return $categories;
    } else {
        // Si no hay resultados, devolvemos un array vacío
        return [];
    }
}

// Funció per mostrar les categories
function mostraCategories($arrayCategories) {

    // Comprovem si hi han categories
    if (!empty($arrayCategories)) {
        echo '<ul>';
        // Mostrem les categories en una llista desordenada
        foreach ($arrayCategories as $category) {

            // Fiquem un link amb la ID de la categoría per trobarla més endavant
            echo '<li><a href="category.php?id=' . $category['id'] . '">' . htmlspecialchars($category['nombre']) . '</a></li>';
        }
        echo '</ul>';
    } else {
        echo '<p>No hi han categories disponibles.</p>';
    }
}
?>
