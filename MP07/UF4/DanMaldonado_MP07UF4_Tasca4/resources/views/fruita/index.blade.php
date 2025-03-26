<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <title>Llista de Fruites</title>
</head>
<body>
    <h1>Llista de Fruites</h1>
    <ul>
        @foreach($fruites as $id => $nom)
            <li><a href="{{ url('/fruita/' . $id) }}">{{ $nom }}</a></li>
        @endforeach
    </ul>

    <h2>Vistes específiques</h2>
    <ul>
        <li><a href="{{ url('/fruita/taronges') }}">Veure Taronges</a></li>
        <li><a href="{{ url('/fruita/peres') }}">Veure Peres</a></li>
    </ul>
</body>
</html>


