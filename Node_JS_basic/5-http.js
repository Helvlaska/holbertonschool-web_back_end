// Module pour créer un serveur
const http = require('http');
// Module pour lire un fichier
const fs = require('fs');

// Fonction qui prend en argument le chemin vers un fichier
function countStudents(path) {
  // Retourne une promesse
  return new Promise((resolve, reject) => {
    // Lecture du fichier en argument de fonction
    fs.readFile(path, 'utf8', (err, data) => {
      // Si lecture impossible renvoie d'un message d'erreur
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Nettoyage et découpage des lignes du fichier lus
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      // Stocker dans une variable le premier élément de chaque ligne
      const students = lines.slice(1);

      // Stock dans une variable une string
      let output = `Number of students: ${students.length}\n`;

      // Création d'une liste vide
      const fields = {};
      // Recherche dans les premiers éléments de chaque ligne
      students.forEach((line) => {
        // Découpe la ligne à chaque virgule
        const parts = line.split(',');
        // Stock dans une variable le premier élément de la ligne
        const firstname = parts[0];
        // Stock dans une variable le quatrième élément de la ligne
        const field = parts[3];

        // Vérifie si le quatrième élément est dans déjà dans la liste
        if (!fields[field]) {
          // Sinon ajouter un dictionnaire vide
          fields[field] = [];
        }
        // Si oui ajouter le premier élément de la ligne dans le dictionnaire
        fields[field].push(firstname);
      });

      // Boucle pour parcourir et renvoyer les dictionnaires
      for (const field in fields) {
        if (Object.hasOwn(fields, field)) {
          const list = fields[field];
          output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
        }
      }

      // Renvoie la string nettoyer
      resolve(output.trim());
    });
  });
}

// Création d'un serveur
const app = http.createServer((req, res) => {
  // Spécification du type de response et d'un code status OK : 200
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Vérifie le chemin de l'url
  if (req.url === '/') {
    // Si ok renvoie un certain message
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    // Sinon en revoie un autre
    res.write('This is the list of our students\n');
    // Récupère le fichier passé en argument
    const database = process.argv[2];
    // Appel de la fonction
    countStudents(database)
      // Manipulation de la donnée récupéré
      .then((output) => {
        res.end(output);
      })
      // Gestion en cas d'erreur
      .catch((err) => {
        res.end(err.message);
      });
  } else {
    // Sinon fermeture de la response
    res.end();
  }
});

// Indication du port utilisé pour faire tourner l'app
app.listen(1245);

// Ligne pour exporter la fonction dans d'autres modules
module.exports = app;
