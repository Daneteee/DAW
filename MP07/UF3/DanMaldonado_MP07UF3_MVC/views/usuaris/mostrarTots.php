<table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
    <thead>
        <tr style="background-color: #f4f4f4;">
            <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Nom</th>
            <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Cognom</th>
            <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Email</th>
            <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Data</th>
        </tr>
    </thead>
    <tbody>
        <!-- Mostrem els usuaris a una taula -->
        <?php while ($usuari = $totsElsUsuaris->fetch_object()): ?>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><?= htmlspecialchars($usuari->nom); ?></td>
                <td style="padding: 10px; border: 1px solid #ddd;"><?= htmlspecialchars($usuari->cognoms); ?></td>
                <td style="padding: 10px; border: 1px solid #ddd;"><?= htmlspecialchars($usuari->email); ?></td>
                <td style="padding: 10px; border: 1px solid #ddd;"><?= htmlspecialchars($usuari->data); ?></td>
            </tr>
        <?php endwhile; ?>
    </tbody>
</table>
