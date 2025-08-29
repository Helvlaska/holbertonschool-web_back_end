export default function updateUniqueItems(map) {
  // Vérifie que map est bien une Map
  if (!(map instanceof Map)) {
    throw new Error("Cannot process");
  }

  // Boucle pour parcourir les éléments de la Map
  for (const [key, value] of map.entries()) {
    // Met à jour les valeurs
    if (value === 1) {
      map.set(key, 100);
    }
  }

  return map;
}
