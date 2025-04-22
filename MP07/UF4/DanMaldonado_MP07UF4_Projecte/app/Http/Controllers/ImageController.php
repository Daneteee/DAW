<?php

namespace App\Http\Controllers;

use App\Models\Image;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Storage;

class ImageController extends Controller
{

    public function create()
    {
        // Formulari per crear una nova imatge
        return view('images.create');
    }

    // Mostrem els detalls d'una imatge
    public function show(Image $image)
    {
        return view('images.show', compact('image'));
    }

    // Mostrem el formulari per editar una imatge
    public function edit(Image $image)
    {
        // Verifiquem que l'usuari actual sigui el propietari de la imatge
        if ($image->user_id != auth()->id()) {
            abort(403, 'Acció no autoritzada.');
        }

        return view('images.edit', compact('image'));
    }

    // Actualitzem una imatge a la base de dades
    public function update(Request $request, Image $image)
    {
        // Validem les dades
        $request->validate([
            'description' => 'nullable|string|max:255',
        ]);

        // Verifiquem que l'usuari actual sigui el propietari de la imatge
        if ($image->user_id != auth()->id()) {
            abort(403, 'Acció no autoritzada.');
        }

        // Actualitzem la imatge si se'n puja una de nova
        if ($request->hasFile('image')) {
            $image->image_path = $request->file('image')->store('images', 'public');
        }

        // Actualitzem la descripció si és necessari
        if ($request->filled('description')) {
            $image->description = $request->description;
        }

        $image->save();

        // Tornem enrere amb un missatge d'èxit
        return redirect()->route('images.show', $image)->with('success', 'Imatge actualitzada correctament.');
    }

    // Eliminem una imatge de la base de dades
    public function destroy(Image $image)
    {
        // Verifiquem que l'usuari actual sigui el propietari de la imatge
        if ($image->user_id != auth()->id()) {
            abort(403, 'Acció no autoritzada.');
        }

        $image->delete();

        // Tornem enrere amb un missatge d'èxit
        return redirect()->route('home')->with('success', 'Imatge eliminada correctament.');
    }

    // Guardem una nova imatge a la base de dades
    public function store(Request $request)
    {
        // Validem les dades
        $request->validate([
            'image' => ['required', 'image', 'max:2048'],
            'description' => ['nullable', 'string', 'max:255'],
        ]);

        // Guardem la imatge al sistema d'emmagatzematge
        $path = $request->file('image')->store('images', 'public');
        
        // Creem un nou registre a la base de dades
        Image::create([
            'user_id' => Auth::id(),
            'image_path' => $path,
            'description' => $request->input('description'),
        ]);

        return redirect()->route('dashboard')->with('status', 'Imatge pujada correctament!');
    }
}
