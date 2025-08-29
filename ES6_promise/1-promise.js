export default function getFullResponseFromAPI(success) {
  // Créer et renvoie une nouvelle promesse
  return new Promise((resolve, reject) => {

    // Vérifie si le paramètre de fonction vaut true ou false
    if (success === true) {
      resolve({status: 200, body:'Success'});
    } else {
      reject(new Error("The fake API is not working currently"));
    }
  });
}
