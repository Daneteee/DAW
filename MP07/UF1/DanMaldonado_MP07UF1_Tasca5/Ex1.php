<?php
// Fes una cookie que desa la data (time stamp)  de la darrera visita en la que un usuari ha estat a la nostra web, 
// i que ens mostri quants minuts, si són més de 60, que ho converteixi a  hores,  o si són més de 24h, a dies fa de
//  la seva darrera visita, en cas que sigui la primera vegada que ens visita, que aparegui un missatge de benvingut. 
//  (Fes una funció per fer els càlculs. Esbrina com php desa la informació en la funció time() per exemple)

function checkLastVisit($timestamp) {
    $darreraVisita = time() - $timestamp;

    if ($darreraVisita < 60) {
        echo "La teva darrera visita ha estat fa " . $darreraVisita . " segons";
    } else if ($darreraVisita >= 60 && $darreraVisita < 3600) {
        $minuts = round($darreraVisita / 60);
        echo "La teva darrera visita ha estat fa " . $minuts . " minuts";
    } else if ($darreraVisita >= 3600 && $darreraVisita < 86400) {
        $hores = round($darreraVisita / 3600);
        echo "La teva darrera visita ha estat fa " . $hores . " hores";
    } else {
        $dies = round($darreraVisita / 86400);
        echo "La teva darrera visita ha estat fa " . $dies . " dies";
    }
}

if (isset($_COOKIE['darrera_visita'])) {
    checkLastVisit($_COOKIE['darrera_visita']);

} else {
    echo "Benvingut a la nostra web! Aquesta és la teva primera visita.";

}

setcookie('darrera_visita', time(), time() + (86400 * 30));
?>