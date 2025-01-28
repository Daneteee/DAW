<?php

function app_autoloader($classname) {
    require_once 'controllers/' .strtolower($classname) . '.php';
}

spl_autoload_register('app_autoloader');

?>