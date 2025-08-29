export default function guardrail(mathFunction) {
  const queue = [];

  try {
    // On essaie d’exécuter la fonction
    const result = mathFunction();
    queue.push(result); // succès → on met le résultat
  } catch (error) {
    // Si erreur → on met le message d'erreur
    queue.push(`Error: ${error.message}`);
  } finally {
    // Toujours exécuté → on ajoute le message final
    queue.push('Guardrail was processed');
  }

  return queue;
}
