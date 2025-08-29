export default function handleResponseFromAPI(promise) {
  // Utilise la promesse reçu en paramètre
  return promise

    // Si la promesse réussit
    .then(() => {
      // Transforme le résultat en un objet
      return { status: 200, body: 'success' };
    })

    // Si la promesse échoue
    .catch(() => {
      // Retourne un objet Error vide
      return new Error();
    })

    // Dans tous les cas (succès ou erreur)
    .finally(() => {
      // Affiche un message dans la console
      console.log("Got a response from the API");
    });
}
