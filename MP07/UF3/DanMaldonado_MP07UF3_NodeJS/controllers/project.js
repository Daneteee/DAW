'use strict'

var Project = require('../models/project');
const fs = require('fs');
const path = require('path');

var controller = {
    // Retornem un missatge simple per la pàgina principal
    home: function(req, res) {
        return res.status(200).send({
            message: "Pàgina home"
        });
    },

    // Retornem un missatge de prova per comprovar el funcionament de l'API
    test: function(req, res) {
        return res.status(200).send({
            message: "Pàgina de test"
        });
    },

    // Creem un nou projecte amb les dades rebudes
    saveProject: function(req, res) {
        var project = new Project();
        var params = req.body;

        // Validació de dades
        if (!params.name || !params.description || !params.category || !params.year || !params.langs) {
            return res.status(400).send({ message: "Tots els camps són obligatoris" });
        }

        if (isNaN(params.year) || params.year < 1900 || params.year > new Date().getFullYear()) {
            return res.status(400).send({ message: "L'any no és vàlid" });
        }

        // Paràmetres rebuts
        project.name = params.name;
        project.description = params.description;
        project.category = params.category;
        project.year = params.year;
        project.langs = params.langs;
        project.image = null;

        // Guardem el projecte a la base de dades
        project.save()
            .then(projectStored => {
                if (!projectStored) {
                    return res.status(404).send({ message: "No s'ha pogut guardar el projecte" });
                }
                return res.status(200).send({ project: projectStored });
            })
            .catch(err => {
                console.error(err);
                return res.status(500).send({ message: "Error en guardar el projecte" });
            });
    },

    // Busquem un projecte per ID a la base de dades
    getProject: function(req, res) {
        var projectId = req.params.id;

        // Busquem el projecte i mostrem un missatge d'estat
        if (!projectId) {
            return res.status(400).send({ message: "No s'ha especificat cap projecte" });
        }

        Project.findById(projectId)
            .then(project => {
                if (!project) {
                    return res.status(404).send({ message: "No s'ha trobat el projecte" });
                }
                return res.status(200).send({ project });
            })
            .catch(err => {
                console.error(err);
                return res.status(500).send({ message: "Error en retornar el projecte" });
            });
    },

    // Obtenim tots els projectes de la base de dades
    getProjects: function(req, res) {
        // Busquem tots els projectes i mostrem error en cas que sigui necessari
        Project.find({})
            .then(projects => {
                if (!projects || projects.length === 0) {
                    return res.status(404).send({ message: "No s'han trobat projectes" });
                }
                return res.status(200).send({ projects });
            })
            .catch(err => {
                console.error(err);
                return res.status(500).send({ message: "Error en retornar els projectes" });
            });

    },

    // Actualitzem un projecte amb la informació rebuda
    updateProject: function(req, res) {
        var projectId = req.params.id;
        var update = req.body;

        // Validació de dades
        if (!update.name || !update.description || !update.category || !update.year || !update.langs) {
            return res.status(400).send({ message: "Tots els camps són obligatoris" });
        }

        if (isNaN(update.year) || update.year < 1900 || update.year > new Date().getFullYear()) {
            return res.status(400).send({ message: "L'any no és vàlid" });
        }

        // Busquem el projecte i amb promeses intentem actualitzar-lo
        Project.findByIdAndUpdate(projectId, update, { new: true })
            .then(updatedProject => {
                if (!updatedProject) {
                    return res.status(404).send({ message: "No s'ha trobat el projecte" });
                }
                return res.status(200).send({ project: updatedProject });
            })
            .catch(err => {
                console.error(err);
                return res.status(500).send({ message: "Error en actualitzar el projecte" });
            });
    },

    // Eliminem un projecte per ID
    deleteProject: function(req, res) {
        var projectId = req.params.id;

        // Busquem el projecte abans d'eliminar-lo
        Project.findById(projectId)
            .then(project => {
                if (!project) {
                    return res.status(404).send({ message: "No s'ha trobat el projecte" });
                }

                // Si el projecte té una imatge, l'eliminem abans de suprimir-lo
                if (project.image) {
                    let imagePath = path.join(__dirname, '../uploads/', project.image);
                    fs.unlink(imagePath, err => {
                        if (err) console.error("Error eliminant la imatge:", err);
                    });
                }

                // Eliminem el projecte
                return Project.findByIdAndDelete(projectId);
            })
            .then(removedProject => {
                if (!removedProject) {
                    return res.status(404).send({ message: "No s'ha trobat el projecte" });
                }
                return res.status(200).send({ project: removedProject });
            })
            .catch(err => {
                console.error(err);
                return res.status(500).send({ message: "Error en eliminar el projecte" });
            });
    },

    // Pugem una imatge
    uploadImage: async function (req, res) {
        // Paràmetres per defecte
        var projectId = req.params.id;
        var fileName = 'Imatge no pujada...';

        if (!req.files || !req.files.image) {
            return res.status(400).send({ message: fileName });
        }

        // Validem la imatge
        try {
            var filePath = req.files.image.path;
            var fileSplit = filePath.split('/');
            var fileName = fileSplit[fileSplit.length - 1];
            var fileExt = fileName.split('.').pop().toLowerCase();

            var validExtensions = ['png', 'jpg', 'jpeg', 'gif'];

            if (!validExtensions.includes(fileExt)) {
                // Eliminem el fitxer si l’extensió no és vàlida
                fs.unlink(filePath, (err) => {
                    if (err) console.error('Error eliminant el fitxer:', err);
                    return res.status(400).send({ message: "L'extensió no és correcta" });
                });
                return;
            }

            // Actualitzem la imatge del projecte
            const projectUpdated = await Project.findByIdAndUpdate(
                projectId,
                { image: fileName },
                { new: true }
            );

            if (!projectUpdated) {
                return res.status(404).send({ message: 'No existeix el projecte' });
            }

            return res.status(200).send({ project: projectUpdated });

        } catch (err) {
            console.error(err);
            return res.status(500).send({ message: 'Error en actualitzar la imatge' });
        }
    }
};

module.exports = controller;
