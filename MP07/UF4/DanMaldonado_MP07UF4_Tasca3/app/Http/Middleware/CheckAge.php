<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class CheckAge
{
    public function handle(Request $request, Closure $next): Response
    {
        $edat = $request->query('edat');

        if (!$edat || $edat < 18) {
            // Fem la redirecció amb el missatge d'error
            return redirect()->route('tasks.index', ['error' => 'No tens l’edat suficient per accedir.']);
        }

        return $next($request);
    }
}




