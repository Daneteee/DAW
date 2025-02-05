'use strict'

var express = require('express');
var ProjectController = require('../controllers/project');

var router = express.Router(); 

var multipart = require('connect-multiparty');

var multipartMiddleware = multipart({ uploadDir: './uploads' });

// Tests
router.get('/home', ProjectController.home);
router.post('/test', ProjectController.test);

// Guardem projecte
router.post('/save-project', ProjectController.saveProject);

// Obtenim projectes
router.get('/project/:id?', ProjectController.getProject);
router.get('/projects', ProjectController.getProjects);

// Actualitzem projecte
router.put('/project/:id', ProjectController.updateProject);

// Eliminem projecte
router.delete('/project/:id', ProjectController.deleteProject);

// Afegim imatge
router.post('/upload-image/:id', multipartMiddleware, ProjectController.uploadImage);

module.exports = router;
