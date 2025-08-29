# 📌 Projet : ES6 Promises

## 📖 Description

Ce projet a pour but d’apprendre et de manipuler les Promises en JavaScript, ainsi que leurs mécanismes associés (then, catch, finally, async/await, gestion des erreurs, etc.).

À la fin, je serais capable d’utiliser les Promises pour gérer des opérations asynchrones de manière fiable et propre.

---

## 🎯 Objectifs d’apprentissage

À la fin de ce projet, je serais capable d’expliquer, sans aide extérieure :

- Les Promises : comment, pourquoi et quand les utiliser
- Comment utiliser les méthodes .then(), .catch() et .resolve()
- Comment utiliser toutes les méthodes de l’objet Promise
- La gestion des erreurs avec throw et try/catch
- L’opérateur await
- Comment utiliser une fonction asynchrone (async function)

---

## ⚙️ Exécution des fichiers

```bash
npm run dev 0-main.js
```

---

## 📑 Liste des tâches et objectifs

0. Keep every promise you make
➝ Créer une fonction getResponseFromAPI() qui retourne une Promise.

1. Don’t make a promise...if you know you can’t keep it
➝ Créer getFullResponseFromAPI(success) qui résout ou rejette une Promise selon un booléen.

2. Catch me if you can!
➝ Gérer une Promise avec .then et .catch, et logguer “Got a response from the API”.

3. Handle multiple successful promises
➝ Exécuter uploadPhoto et createUser en parallèle et afficher leur résultat combiné.

4. Simple promise
➝ Créer signUpUser(firstName, lastName) qui retourne une Promise résolue avec un objet utilisateur.

5. Reject the promises
➝ Créer uploadPhoto(filename) qui retourne une Promise rejetée avec une erreur.

6. Handle multiple promises
➝ Créer handleProfileSignup(firstName, lastName, fileName) qui retourne le statut de plusieurs Promises via Promise.allSettled.

7. Load balancer
➝ Créer loadBalancer(chinaDownload, USDownload) qui retourne la première Promise résolue.

8. Throw an error
➝ Créer divideFunction(numerator, denominator) qui divise ou lance une erreur si le dénominateur est 0.

9. Throw error / try catch
➝ Créer guardrail(mathFunction) qui exécute une fonction, capture ses erreurs, et ajoute “Guardrail was processed”.
