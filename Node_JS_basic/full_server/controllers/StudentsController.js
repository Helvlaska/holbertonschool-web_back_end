const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const database = process.argv[2];

    readDatabase(database)
      .then((fields) => {
        let output = 'This is the list of our students\n';

        // Étape 1 : récupérer les clés de l’objet
        const keys = Object.keys(fields);

        // Étape 2 : fonction de comparaison insensible à la casse
        function compareFields(a, b) {
          return a.toLowerCase().localeCompare(b.toLowerCase());
        }

        // Étape 3 : trier les clés avec la fonction
        const sortedFields = keys.sort(compareFields);

        sortedFields.forEach((field) => {
          const list = fields[field];
          output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
        });

        res.status(200).send(output.trim());
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((fields) => {
        const list = fields[major] || [];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
