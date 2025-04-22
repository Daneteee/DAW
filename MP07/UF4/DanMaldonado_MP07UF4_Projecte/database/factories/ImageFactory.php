<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use App\Models\User;

class ImageFactory extends Factory
{
    public function definition(): array
    {
        // Obtenim tots els fitxers de la carpeta d'imatges
        $files = glob(storage_path('app/public/images/*.*'));

        // Seleccionem una imatge aleatòria si existeixen fitxers
        $image = count($files) ? 'images/' . basename($files[array_rand($files)]) : null;

        // Generem una imatge amb un usuari associat i una descripció
        return [
            'user_id' => User::factory(),
            'image_path' => $image, 
            'description' => fake()->sentence(), 
        ];
    }
}