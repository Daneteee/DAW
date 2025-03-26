<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <title>Espardenya</title>
</head>
<body>
    <h1>Detalls de l'Espardenya</h1>
    <p><strong>Marca:</strong> {{ $espardenya['marca'] }}</p>
    <p><strong>Model:</strong> {{ $espardenya['model'] }}</p>
    <p><strong>Color:</strong> {{ $espardenya['color'] }}</p>
    <p><strong>Stock:</strong> {{ $espardenya['stock'] ? 'Disponible' : 'No disponible' }}</p>

    <a href="{{ url('/espardenya') }}">Tornar a la llista</a>
</body>
</html>

