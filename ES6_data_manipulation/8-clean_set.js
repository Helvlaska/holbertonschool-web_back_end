export default function cleanSet(set, startString) {
  // Vérifie si startString est vide
  if (startString === "") {
    return "";
  }

  const cleanValue = [];           // Création d'une variable pour stocker les nouvelles values

  for (const value of set) {        // Boucle pour parcourir les valeurs du set
    if (value.startsWith(startString)) {    // Vérifie si value commence par startString
      const cleanStartValue = value.slice(startString.length);   // Retire startString de value
      cleanValue.push(cleanStartValue);     // Envoie des nouvelles values dans le tableau
    }
  }

  return cleanValue.join("-");                // Retourne la nouvelle string fromatée
}
