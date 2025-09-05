// Permet de lire une fichier csv
const fs = require('fs');

// Fonction qui prends en argument le chemin d'accès d'un fichier csv
function countStudents(path) {
  // Lecture du fichier path
  try {
    // Stock le contenu du fichier dans une variable
    const data = fs.readFileSync(path, 'utf8');
    // 'Nettoie' les données : les lignes vides et les espaces
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    // Enlève la première ligne du fichier csv (juste un modèle de donnée)
    const students = lines.slice(1);

    // Affiche dans la console le nombre d'étudiants
    console.log(`Number of students: ${students.length}`);

    // Création liste vide pour stocker le nom des fillières
    const fields = {};
    // Recherche dans les étudiants du fichier csv pour chaque ligne
    students.forEach((line) => {
      // Découpe chaque ligne en parties
      const parts = line.split(',');
      // La 1er partie c'est le Prénom
      const firstname = parts[0];
      // La 3e partie c'est la fillière
      const field = parts[3];

      // Vérifie si la fillière est déjà dans la liste
      if (!fields[field]) {
        // Sinon créer un dictionnaire vide
        fields[field] = [];
      }
      // Si oui ajouter le prénom de l'étudiant
      fields[field].push(firstname);
    });

    // Boucle pour lire chaque liste de fillière
    for (const field in fields) {
      if (Object.hasOwn(fields, field)) {
        const list = fields[field];
        console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

// Ligne pour exporter et utiliser la fonction dans d'autres fichiers
module.exports = countStudents;
