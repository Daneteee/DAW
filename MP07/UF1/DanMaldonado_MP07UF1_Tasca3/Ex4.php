<?php
# Teniu dues matrius com la següent. Una conté etiquetes i l’altra conté valors. Escriviu un programa per generar la tercera matriu associativa.
include ("header.php");

# Arrays
$keys = array(
    "field1"=>"first",
    "field2"=>"second",
    "field3"=>"third"
);
$values = array(
    "field1value"=>"dinosaur",
    "field2value"=>"pig",
    "field3value"=>"platypus"
);

# Creem la array amb claus i valors
$keysAndValues = array();
foreach ($keys as $key => $value) {
    $keysAndValues[$value] = $values[$key."value"];
}
# Mostrem per pantalla
foreach ($keysAndValues as $clau => $valor) {
    echo "$clau: $valor<br>";
}

echo "<br>";

# Amb combine
$claus_combinada = array_values($keys);
$valors_combinada = array_values($values);

$array_combinada = array_combine($claus_combinada, $valors_combinada);

# Mostrem per pantalla
foreach ($array_combinada as $clau_comb => $valo_comb) {
    echo "$clau_comb: $valo_comb<br>";
}
include ("footer.php");
?>
