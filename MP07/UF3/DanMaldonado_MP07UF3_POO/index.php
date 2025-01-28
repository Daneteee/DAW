<?php

require_once 'autoloader.php';

// Crear autors
$autor1 = new Autor("James", "Dashner");
$autor2 = new Autor("Tana", "Franch");

// Crear llibres
$llibre1 = new Llibre("El destello", $autor1, "123456789");
$llibre2 = new Llibre("La ultima noche de Rose Daly", $autor2, "987654321");

// Afegir llibres als autors
$autor1->afegirLlibre($llibre1);
$autor2->afegirLlibre($llibre2);

// Crear biblioteca
$biblioteca = new Biblioteca();
$biblioteca->afegirLlibre($llibre1);
$biblioteca->afegirLlibre($llibre2);

// Crear usuari
$usuari = new Usuari("Joan", "Garcia");

// Interacció amb la biblioteca
echo "<html><body>";
echo "<h1>Biblioteca Virtual</h1>";

echo "<h2>Catàleg inicial</h2>";
echo "<pre>";
$biblioteca->mostrarCataleg();
echo "</pre>";

echo "<h2>Préstec de llibres</h2>";
echo "<pre>";
$usuari->prestarLlibre($llibre1);
$usuari->mostrarLlibresPrestats();
echo "</pre>";

echo "<h2>Retorn de llibres</h2>";
echo "<pre>";
$usuari->retornarLlibre($llibre1);
$usuari->mostrarLlibresPrestats();
echo "</pre>";

echo "<h2>Catàleg final</h2>";
echo "<pre>";
$biblioteca->mostrarCataleg();
echo "</pre>";

echo "</body></html>";