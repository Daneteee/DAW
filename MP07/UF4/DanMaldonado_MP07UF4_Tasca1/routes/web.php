<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome', [
        'uf' => 'Uf4: Laravel',
        'tasca' => 'tasca 1'
    ]);
})->name('home');



Route::get('/pelicula/{titol?}/{any?}', function ($titol = 'No has posat cap títol', $any = 2022) {
    // Amb el compact creem una array associativa amb les variables que li passem
    return view('pelicula', compact('titol', 'any'));
})->where([
    'titol' => '[A-Za-zÀ-ÿ\s]+', 
    'any' => '\d{4}' 
])->name('pelicula');

Route::pattern('codi_postal', '\d{5}');

Route::get('/ubicacio/{codi_postal}', function ($codi_postal) {
    return "Codi postal: $codi_postal";
});

Route::get('/servei/{codi_postal}', function ($codi_postal) {
    return "Serveis disponibles per al codi postal: $codi_postal";
});

Route::fallback(function () {
    return 'Això és un missatge personalitzat. I et vull dir que no he pogut trobar la pagina que busques. 
    404 Not found my friend.';
});

