export default function createIn8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);   // Création d'un buffer
  const view = new DataView(buffer);        // Interpréter le buffer

  // Vérifie si la position n'est pas hors champ
  if (position >= length) {
    throw new Error("Position outside range");  // Envoie erreur si oui
  } else {
    view.setInt8(position, value);  // Sinon ajoute la value à une position donnée
  }

  return view;  // Retourne le nouveau tableau
}
