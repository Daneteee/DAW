<?php

require_once'autoloader.php';

// Demostració del funcionament
$autor = new Autor("J.K.", "Rowling");
$llibre1 = new Llibre("Harry Potter i la pedra filosofal", $autor, "1234567890");
$llibre2 = new Llibre("Harry Potter i la cambra secreta", $autor, "0987654321");

$autor->afegirLlibre($llibre1);
$autor->afegirLlibre($llibre2);

$biblioteca = new Biblioteca();
$biblioteca->afegirLlibre($llibre1);
biblioteca->afegirLlibre($llibre2);

$usuari = new Usuari("Joan", "Pérez");

echo "Catàleg de la biblioteca:\n";
biblioteca->mostrarCataleg();

echo "\nUsuari pren un llibre:\n";
$usuari->prestarLlibre($llibre1);

echo "\nCatàleg actualitzat:\n";
biblioteca->mostrarCataleg();

echo "\nLlibres prestats per l'usuari:\n";
$usuari->mostrarLlibresPrestats();

$usuari->retornarLlibre($llibre1);

echo "\nLlibres prestats després de retornar:\n";
$usuari->mostrarLlibresPrestats();

echo "\nCatàleg final:\n";
biblioteca->mostrarCataleg();
