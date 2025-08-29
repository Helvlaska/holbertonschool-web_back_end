export default function signUpUser(firstName, lastName) {
  // Retourne une promesse résolue
  return Promise.resolve({
    firstName,
    lastName,
  });
}
