<?php

namespace Database\Seeders;

use App\Models\User;
use App\Models\Image;
use App\Models\Like;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        // Creem 3 usuaris
        User::factory(3)->create()->each(function ($user) {
            // Creem 5 imatges per a cada usuari
            Image::factory(5)->create(['user_id' => $user->id])->each(function ($image) use ($user) {
                // Creem un nombre aleatori de like per a cada imatge
                $likesCount = rand(1, 5); 
                $users = User::all(); // Obtenim tots els usuaris
                $likesCount = min($likesCount, $users->count()); // Assegurem que no sol·licitem més usuaris dels que existeixen
                $likedUsers = $users->random($likesCount)->pluck('id'); // Seleccionem usuaris aleatoris

                foreach ($likedUsers as $likedUserId) {
                    // Fem que l'usuari no es doni like a si mateix
                    if ($likedUserId != $user->id) {
                        Like::factory()->create([
                            'user_id' => $likedUserId,
                            'image_id' => $image->id,
                        ]);
                    }
                }
            });

            // Creem comentaris aleatoris per a cada imatge
            Image::where('user_id', $user->id)->each(function ($image) use ($user) {
                $commentCount = rand(1, 3); 

                foreach (range(1, $commentCount) as $index) {
                    // Creem comentaris d'usuaris aleatoris
                    $commentingUser = User::all()->random();
                    \App\Models\Comment::factory()->create([
                        'user_id' => $commentingUser->id,
                        'image_id' => $image->id,
                        'content' => fake()->sentence(),
                    ]);
                }
            });
        });
    }
}
