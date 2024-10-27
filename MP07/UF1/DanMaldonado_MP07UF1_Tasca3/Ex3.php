<?php
# Fes uns script PHP que calculi la temperatura mitjana, les 5 més fredes i les 5 més altes (en Celsius):
include("header.php");

$temperaturesFahrenheit = array(78, 60, 62, 68, 71, 68, 73, 85, 66, 64, 76, 63, 75, 76, 73, 68, 62, 73, 72, 65, 74, 62, 62, 65, 64, 68, 73, 75, 79, 73);

// Mostra les temperatures en Fahrenheit
echo "Temperatures en Fahrenheit: " . implode(", ", $temperaturesFahrenheit) . "";

echo "<br>";

// Transformem a celsius
$temperaturesCelsius = array_map(function($tempF) {
    return round(($tempF - 32) * 5 / 9);
}, $temperaturesFahrenheit);

// Ordenem temperatures
sort($temperaturesFahrenheit);
sort($temperaturesCelsius);

// Agafem las 5 més fredes
$fredes = array_slice($temperaturesFahrenheit, 0, 5);
echo "5 més fredes: " . implode(", ", $fredes) . "";

// Agafem les 5 més calentes
$calentes = array_slice($temperaturesFahrenheit, -5);
echo "<br>5 més calentes: " . implode(", ", $calentes) . "";

// Fem la mitjana
$mitjanaFahrenheit = array_sum($temperaturesFahrenheit) / count($temperaturesFahrenheit);
echo "<br>Temperatura mitjana en Fahrenheit: " . round($mitjanaFahrenheit, 2);


echo "<br><br>";

// Mostrar celsius
echo "Temperatures en Celsius: " . implode(", ", $temperaturesCelsius) . "";
echo "<br>";

// Agafem las 5 més fredes
$fredes = array_slice($temperaturesCelsius, 0, 5);
echo "5 més fredes: " . implode(", ", $fredes) . "";

// Agafem les 5 més calentes
$calentes = array_slice($temperaturesCelsius, -5);
echo "<br>5 més calentes: " . implode(", ", $calentes) . "";

// Fem la mitjana
$mitjanaCelsius = array_sum($temperaturesCelsius) / count($temperaturesCelsius);
echo "<br>Temperatura mitjana en Celsius: " . round($mitjanaCelsius, 2);

include("footer.php");
?>
