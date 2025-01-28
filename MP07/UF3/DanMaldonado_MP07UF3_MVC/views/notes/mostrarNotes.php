<table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
    <thead>
        <tr style="background-color: #f4f4f4;">
            <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Nom</th>
            <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Contingut</th>
        </tr>
    </thead>
    <tbody>
        <!-- Mostrem les notes a una taula -->
        <?php while ($nota = $totesLesNotes->fetch_object()): ?>
            <tr>
                <td style="padding: 10px; border: 1px solid #ddd;"><?= htmlspecialchars($nota->nom); ?></td>
                <td style="padding: 10px; border: 1px solid #ddd;"><?= htmlspecialchars($nota->contingut); ?></td>
            </tr>
        <?php endwhile; ?>
    </tbody>
</table>
