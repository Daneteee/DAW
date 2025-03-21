'use strict'

var express = require('express');
var bodyParser = require('body-parser');

var app = express();

//carregar rutes

var project_routes = require('./routes/project');


//middlewares
// codifiquem a json tot el que ens arriba
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));



// CORS

// Configurar capçaleress y cors
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Authorization, X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Request-Method');
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
    res.header('Allow', 'GET, POST, OPTIONS, PUT, DELETE');
    next();
});



//rutes

app.use('/api',project_routes);

//exportar

module.exports = app;







