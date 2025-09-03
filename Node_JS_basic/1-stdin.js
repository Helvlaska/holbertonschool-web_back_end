// Affiche la question dans la console
console.log("Welcome to Holberton School, what is your name?");

// Permet au user de faire une entrée de donnée
process.stdin.on("data", (data) => {
  // Convertie la donnée en string et la nettoie des espaces
  const name = data.toString().trim();
  console.log(`Your name is: ${name}`);
  console.log("This important software is now closing");
  // Ferme l'entrée de données
  process.exit();
})
