<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Image;

class LikeController extends Controller
{
    // Afegim o eliminem un like d'una imatge
    public function toggle(Image $image)
    {
        $user = auth()->user();

        // Comprovem si l'usuari ja ha fet like a la imatge
        if ($image->likes()->where('user_id', $user->id)->exists()) {
            // Eliminem el like
            $image->likes()->where('user_id', $user->id)->delete();

            // Retornem la resposta amb l'estat actualitzat
            return response()->json(['liked' => false, 'likes_count' => $image->likes()->count()]);
        } else {
            // Afegim un like
            $image->likes()->create(['user_id' => $user->id]);

            // Retornem la resposta amb l'estat actualitzat
            return response()->json(['liked' => true, 'likes_count' => $image->likes()->count()]);
        }
    }
}
