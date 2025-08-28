export default function hasValuesFromArray(set, array) {
  for (const i of array) {      // Boucle sur le tableau
    if (!set.has(i)) {          // Vérifie si la value du tableau n'est pas dans le set
      return false;             // Si un n'y est pas return False
    }
  }
  return true;                  // Si tout est OK return True
}
