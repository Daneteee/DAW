<?php

namespace App\Http\Controllers;

use App\Http\Requests\ProfileUpdateRequest;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Redirect;
use Illuminate\View\View;

class ProfileController extends Controller
{
    // Mostrem el formulari del perfil de l'usuari
    public function edit(Request $request): View
    {
        // Retornem la vista per editar el perfil amb les dades de l'usuari
        return view('profile.edit', [
            'user' => $request->user(),
        ]);
    }

    // Actualitzem la informació del perfil de l'usuari
    public function update(ProfileUpdateRequest $request): RedirectResponse
    {
        $user = $request->user();

        // Omplim les dades de l'usuari amb les dades validades
        $user->fill($request->validated());

        // Si l'email ha canviat, eliminem la verificació
        if ($user->isDirty('email')) {
            $user->email_verified_at = null;
        }

        // Si s'ha pujat una nova imatge, la guardem i actualitzem el perfil
        if ($request->hasFile('image')) {
            $imagePath = $request->file('image')->store('profile_photos', 'public');
            $user->image = $imagePath; 
        }

        // Guardem els canvis al perfil de l'usuari
        $user->save();

        // Tornem enrere amb un missatge d'èxit
        return Redirect::route('profile.edit')->with('status', 'profile-updated');
    }

    // Eliminem el compte de l'usuari
    public function destroy(Request $request): RedirectResponse
    {
        // Validem la contrasenya abans d'eliminar el compte
        $request->validateWithBag('userDeletion', [
            'password' => ['required', 'current_password'],
        ]);

        $user = $request->user();

        // Tanquem la sessió de l'usuari
        Auth::logout();

        // Eliminem el compte de l'usuari
        $user->delete();

        // Invalidem la sessió i regenerem el token CSRF
        $request->session()->invalidate();
        $request->session()->regenerateToken();

        // Redirigim a la pàgina principal
        return Redirect::to('/');
    }
}