export default function cleanSet(set, startString) {
  // Vérifie si startString est une string vide
  if (startString === '') return '';

  const arrayFromSet = Array.from(set);     // Transforme le set en array

  // Garder que les values qui commencent par startString
  const filtered = arrayFromSet.filter(value => value.startsWith(startString));

  // Retire startString des values
  const cleaned = filtered.map(value => value.slice(startString.length));

  // Formatage de la string
  const result = cleaned.join('-');

  return result;
}
