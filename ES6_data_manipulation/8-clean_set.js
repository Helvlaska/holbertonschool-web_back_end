export default function cleanSet(set, startString) {
  // Vérifie si startString est vide ou n'est pas de type string
  if (startString === "" || typeof startString !== "string") {
    return "";
  }

  // Création d'un array pour stocker les nouvelles values
  const cleanValue = [];

  // Boucle pour parcourir les valeurs du set
  for (const value of set) {
    // Vérifie si value commence par startString et si de type string
    if (value.startsWith(startString) && typeof value === "string") {
      // Retire startString de value
      const cleanStartValue = value.slice(startString.length);
      // Envoie des nouvelles values dans le tableau
      cleanValue.push(cleanStartValue);
    }
  }
  // Retourne la nouvelle string fromatée et réassemblée
  return cleanValue.join("-");
}
