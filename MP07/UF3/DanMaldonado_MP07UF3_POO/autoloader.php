<?php
function app_loader($class){
    var_dump($class);
    require_once strtolower($class) .'.php';
}

spl_autoload_register('app_loader');