// Import de express
const express = require('express');

// Création d'une instance de l'app
const app = express();

// Définition d'une route GET
app.get('/', (req, res) => {
  // Retourne une réponse string
  res.send('Hello Holberton School!');
});

// Lancer le serveur sur un port
app.listen(1245);

// Ligne pour exporter app dans d'autres modules
module.exports = app;
