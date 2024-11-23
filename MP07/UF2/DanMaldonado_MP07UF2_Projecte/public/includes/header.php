<?php
session_start();
require_once 'helpers.php'; 
require_once 'db_connection.php'; 

$categories = llistarCategories($db);
?>
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header>
    <h1>DaneBlog</h1>
</header>

<!-- Categories -->
<nav class="categories-bar">
    <?php mostraCategories($categories); ?>
</nav>
