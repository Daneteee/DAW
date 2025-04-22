<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use App\Models\User;
use App\Models\Image;

class LikeFactory extends Factory
{
    public function definition(): array
    {
        // Generem un like amb un usuari i una imatge associats
        return [
            'user_id' => User::factory(),
            'image_id' => Image::factory(), 
        ];
    }
}