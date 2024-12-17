<?php
if (!isset($_SESSION)) {
    session_start();
}

require_once __DIR__ . '/../helpers.php'; 
require_once __DIR__ . '/../config/db.php'; 


$categories = llistarCategories($db);
?>
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css" rel="stylesheet">

</head>
<body>
<header>
    <h1><a href="/index.php" style="color: white; text-decoration: none;">DaneBlog</a></h1>
</header>

<!-- Categories -->
<nav class="categories-bar">
    <?php mostraCategories($categories); ?>
</nav>
