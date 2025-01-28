<!-- /views/notes/crearNota.php -->
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crear Nota</title>
</head>
<body>
    <h2>Titol: <?= htmlspecialchars($nota->getNom()); ?></h2>
    <h3>Descripció: <?= htmlspecialchars($nota->getContingut()); ?></h3>
</body>
</html>
