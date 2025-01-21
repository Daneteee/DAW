<?php

class Conectat{
    public static function conexio(){
        $con = new mysqli("localhost", "root", "", "prova");
        $con->query("SET NAMES 'utf8'");
        return $con;
    }
}

?>