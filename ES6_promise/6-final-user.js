import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ])
    .then((result) => result.map((result) => {
      // Si la promesse a été résolue avec succès
      if (result.status === "fulfilled") {
        return { status: 'fulfilled', value: result.value };
      }
      // Si la promesse a été rejetée, on retourne la raison sous forme de string
      return { status: 'rejected', value: result.reason.toString() };
    }));
}
