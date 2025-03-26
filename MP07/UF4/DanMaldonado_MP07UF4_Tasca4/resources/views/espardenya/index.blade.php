<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <title>Llista d'espardenyes</title>
</head>
<body>
    <h1>Llista d'Espardenyes</h1>
    <ul>
        @foreach($espardenyes as $id => $espardenya)
            <li>
                <a href="{{ url('/espardenya/' . $id) }}">
                    {{ $espardenya['marca'] }} - {{ $espardenya['model'] }} ({{ $espardenya['color'] }})
                </a>
            </li>
        @endforeach
    </ul>
</body>
</html>


