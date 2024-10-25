<?php

# logout.php Fer la pàgina de logout que s’hi accedeix si es prem el botó de logout, o bé si s’ha acabat la sessió (d’1 minut com a màxim). 
# On es destrueix la sessió i es mostra un missatge que diu fins la propera. I hi ha un link a index.php

session_start();

# Destruïm la sessió
session_destroy();
echo '<h1>Fins la propera!</h1>
    <a href="index.php">Tornar a la pàgina principal</a>';
?>

