<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class EspardenyaController extends Controller
{
    private $espardenyes = [
        1 => [
            'marca' => 'Adidas',
            'model' => 'Stan Smith',
            'color' => 'Blanc',
            'stock' => true
        ],
        2 => [
            'marca' => 'Nike',
            'model' => 'Air Force 1',
            'color' => 'Negre',
            'stock' => false
        ],
        3 => [
            'marca' => 'Puma',
            'model' => 'Suede Classic',
            'color' => 'Vermell',
            'stock' => true
        ]
    ];

    // Mostra la llista de totes les espardenyes
    public function index()
    {
        return view('espardenya.index', ['espardenyes' => $this->espardenyes]);
    }

    // Mostra una espardenya concreta
    public function show($id)
    {
        if (!isset($this->espardenyes[$id])) {
            abort(404);
        }
        return view('espardenya.show', ['espardenya' => $this->espardenyes[$id]]);
    }
}
