<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\FruitaController;
use App\Http\Controllers\EspardenyaController;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/fruita', [FruitaController::class, 'index']);
Route::get('/fruita/taronges', [FruitaController::class, 'taronges']);
Route::get('/fruita/peres', [FruitaController::class, 'peres']);
Route::get('/fruita/{id}', [FruitaController::class, 'show']);

Route::resource('espardenya', EspardenyaController::class)->except(['edit']);


