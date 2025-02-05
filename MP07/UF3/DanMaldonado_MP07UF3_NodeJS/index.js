'use strict'

var mongoose = require('mongoose');
var app = require('./app');
var port = 3700;


// Connexió a la BBDD
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost:27017/portfolio')
    .then(() => {
        console.log("Connexió a la BBDD establerta amb èxit...");

        // Creació del servidor web
        app.listen(port, () => {
            console.log("Servidor corriendo correctamente en la url: localhost:3700");
        });
    })
    .catch(err => console.log(err));

