<?php
function app_loader($class){
    require_once strtolower($class) .'.php';
}

spl_autoload_register('app_loader');