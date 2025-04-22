<?php

namespace App\Http\Controllers;

use App\Models\Image;
use Illuminate\Http\Request;

class HomeController extends Controller
{
    // Mostrem la pàgina principal amb les imatges
    public function index()
    {
        // Obtenim les imatges amb la informació de l'usuari
        $images = Image::with('user')
            ->orderBy('created_at', 'desc') // Ordenem per data de creació, de més recent a més antiga
            ->paginate(5); // Paginem les imatges, 5 per pàgina

        return view('home', compact('images'));
    }
}
