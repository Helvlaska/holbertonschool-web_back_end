// module pour créer un serveur
const http = require('http');

// Créer le serveur
const app = http.createServer((req, res) => {
  // La réponse est un texte brut avec un code OK 200
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  // Envoie un message en console et termine la réponse
  res.end('Hello Holberton School!');
});

// Demande au serveur de rester à l'écoute
app.listen(1245);

// Permet l'exportation de la fonction dans d'autres modules
module.exports = app;
