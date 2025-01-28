<?php

class Conectat{
    public static function conexio(){
        $con = new mysqli("localhost", "root", "123", "notes_m7");
        $con->query("SET NAMES 'utf8'");
        return $con;
    }
}

?>