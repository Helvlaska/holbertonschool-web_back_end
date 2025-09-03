// Affiche un message en console
process.stdout.write("Welcome to Holberton School, what is your name?\n");

// Permet l'entré de données par le user
process.stdin.on("data", (data) => {
  // Affiche le message en console avec la nouvelle donnée
  process.stdout.write(`Your name is: ${data}`);
});

// Fermeture de l'entrée de donnée
process.stdin.on("end", () => {
  // Affiche du message de fermeture
  process.stdout.write("This important software is now closing\n");
});
