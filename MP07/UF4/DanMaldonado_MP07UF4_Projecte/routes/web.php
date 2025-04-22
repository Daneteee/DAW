<?php

use App\Http\Controllers\ProfileController;
use App\Http\Controllers\HomeController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ImageController;
use App\Http\Controllers\CommentController;
use App\Http\Controllers\LikeController;

// Ruta principal
Route::get('/', function () {
    return view('welcome');
});

// Ruta del dashboard
Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

// Rutes amb autenticació
Route::middleware('auth')->group(function () {
    // Ruta pàgina principal
    Route::get('/home', [HomeController::class, 'index'])->name('home');

    // Rutes perfil usuari
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');

    // Rutes imatges
    Route::get('/images/create', [ImageController::class, 'create'])->name('images.create');
    Route::post('/images', [ImageController::class, 'store'])->name('images.store');
    Route::get('/images/{image}', [ImageController::class, 'show'])->name('images.show');
    Route::get('/images/{image}/edit', [ImageController::class, 'edit'])->name('images.edit');
    Route::put('/images/{image}', [ImageController::class, 'update'])->name('images.update');
    Route::delete('/images/{image}', [ImageController::class, 'destroy'])->name('images.destroy');

    // Rutes comentaris
    Route::post('/images/{image}/comments', [CommentController::class, 'store'])->name('comments.store');
    Route::put('/comments/{comment}', [CommentController::class, 'update'])->name('comments.update');
    Route::delete('/comments/{comment}', [CommentController::class, 'destroy'])->name('comments.destroy');

    // Ruta "m'agrada"
    Route::post('/images/{image}/like', [LikeController::class, 'toggle'])->name('images.like');
});

// Rutes d'autenticació
require __DIR__.'/auth.php';