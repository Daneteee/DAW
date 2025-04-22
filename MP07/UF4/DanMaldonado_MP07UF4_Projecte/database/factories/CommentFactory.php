<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use App\Models\User;
use App\Models\Image;

class CommentFactory extends Factory
{
    public function definition(): array
    {
        // Generem un comentari amb un usuari i una imatge associats
        return [
            'user_id' => User::factory(), 
            'image_id' => Image::factory(), 
            'content' => $this->faker->sentence(), 
        ];
    }
}