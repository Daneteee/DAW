<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FruitaController extends Controller
{
    private $fruites = [
        1 => "Préssec",
        2 => "Plàtan",
        3 => "Taronja",
        4 => "Pera",
        5 => "Cirera",
        6 => "Raïm",
        7 => "Síndria",
        8 => "Meló",
        9 => "Kiwi",
        10 => "Maduixa"
    ];

    public function index()
    {
        return view('fruita.index', ['fruites' => $this->fruites]);
    }

    // Mostrem una fruita específica per ID
    public function show($id)
    {
        if (!isset($this->fruites[$id])) {
            abort(404);
        }
        return view('fruita.show', ['fruita' => $this->fruites[$id]]);
    }

    public function taronges()
    {
        return view('fruita.taronges', ['fruita' => 'Taronja']);
    }

    public function peres()
    {
        return view('fruita.peres', ['fruita' => 'Pera']);
    }
}


