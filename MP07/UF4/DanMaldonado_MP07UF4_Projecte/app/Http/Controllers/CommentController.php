<?php

namespace App\Http\Controllers;

use App\Models\Comment;
use App\Models\Image;
use Illuminate\Http\Request;

class CommentController extends Controller
{
    // Afegim un nou comentari a una imatge
    public function store(Request $request, $imageId)
    {
        $request->validate([
            'content' => 'required|string'
        ]);

        $comment = new Comment();
        $comment->user_id = auth()->id();
        $comment->image_id = $imageId;
        $comment->content = $request->input('content');
        $comment->save();

        // Tornem enrere amb un missatge d'èxit
        return redirect()->back()->with('success', 'Comentari afegit!');
    }

    // Actualitzem un comentari existent
    public function update(Request $request, Comment $comment)
    {
        // Comprovem si l'usuari actual és el propietari del comentari
        if ($comment->user_id != auth()->id()) {
            abort(403);
        }

        $request->validate([
            'content' => 'required|string'
        ]);

        $comment->content = $request->input('content');
        $comment->save();

        return redirect()->back()->with('success', 'Comentari actualitzat!');
    }

    // Eliminem un comentari existent
    public function destroy(Comment $comment)
    {
        // Comprovem si l'usuari actual és el propietari del comentari
        if ($comment->user_id != auth()->id()) {
            abort(403);
        }

        $comment->delete();

        return redirect()->back()->with('success', 'Comentari eliminat!');
    }
}
