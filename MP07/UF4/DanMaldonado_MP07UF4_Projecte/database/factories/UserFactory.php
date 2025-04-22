<?php

namespace Database\Factories;

use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;

class UserFactory extends Factory
{
    // Definim la contrasenya actual que utilitzem a la fàbrica
    protected static ?string $password;

    // Definim l'estat per defecte del model
    public function definition(): array
    {
        return [
            'name' => fake()->firstName(), 
            'surname' => fake()->lastName(),
            'nick' => fake()->unique()->userName(), 
            'email' => fake()->unique()->safeEmail(), 
            'password' => bcrypt('password'), 
            'image' => fake()->imageUrl(300, 300, 'people'), // Generem una URL d'imatge aleatòria
            'role' => 'user',
        ];
    }

    // Indiquem que l'adreça de correu electrònic del model no hauria d'estar verificada
    public function unverified(): static
    {
        return $this->state(fn (array $attributes) => [
            'email_verified_at' => null,
        ]);
    }
}