# 📦 Projet : ES6 Basic (Holberton – Web Back End)

## 🎯 Objectifs d’apprentissage

- Comprendre const vs let et la portée de bloc.
- Utiliser arrow functions, paramètres par défaut, rest et spread.
- Maîtriser template literals et les raccourcis d’objets (propriétés, méthodes, clés calculées).
- Pratiquer for...of et manipuler des objets/itérables.

## ✅ Prérequis

- Ubuntu 20.04 LTS (ou équivalent)
- Node.js v20.x et npm ≥ 10
- Git

## ▶️ Exécution locale

Les exemples d’exécution fournis par l’énoncé appellent :

```bash
npm run dev 0-main.js
```

## 🗂️ Arborescence

ES6_basic/
├── 0-constants.js
├── 0-main.js
├── 1-block-scoped.js
├── 1-main.js
├── 2-arrow.js
├── 2-main.js
├── 3-default-parameter.js
├── 3-main.js
├── 4-rest-parameter.js
├── 4-main.js
├── 5-spread-operator.js
├── 5-main.js
├── 6-string-interpolation.js
├── 6-main.js
├── 7-getBudgetObject.js
├── 7-main.js
├── 8-getBudgetCurrentYear.js
├── 8-main.js
├── 9-getFullBudget.js
├── 9-main.js
├── 10-loops.js
├── 10-main.js
├── 11-createEmployeesObject.js
├── 11-main.js
├── 12-createReportObject.js
├── 12-main.js
├── package.json
├── babel.config.js
└── .eslintrc.js

## 📋 Tâches (résumé & attentes)

- Task 0 : Const or let?

  - Remplacer var par const/let.
  - taskFirst : chaîne fixe → const.
  - taskNext : on concatène progressivement → let.

---

- Task 1 : Block Scope

  - Éviter d’écraser les valeurs extérieures dans le if.
  - Utilise const/let dans le bloc pour préserver [false, true] en sortie quand trueOrFalse === true.

---

- Task 2 : Arrow functions

  - Supprimer const self = this.
  - Définir addNeighborhood en arrow pour capturer le this de l’instance.

---

- Task 3 : Parameter defaults

  - Écrire la fonction en une ligne en donnant des valeurs par défaut à expansion1989 et expansion2019 (89 et 19).

---

- Task 4 : Rest parameter

  - Retourner le nombre d’arguments passés via (...args) → args.length.

---

- Task 5 : Spread syntax

  - Concaténer array1, array2, et chaque lettre de string en une seule ligne avec [...array1, ...array2, ...string].

---

- Task 6 : Template literals

  - Réécrire le return avec des backticks et ${} au lieu des +.

---

- Task 7 : Object property shorthand

  - Utiliser { income, gdp, capita }.

---

- Task 8 : Computed property names

  - Créer l’objet directement avec des clés dynamiques income-year, etc., sans remplir après coup.

---

- Task 9 : ES6 method properties

  - Dans fullBudget, réécrire les fonctions en syntaxe méthode : getIncomeInDollars(income) { ... }.

---

- Task 10 : For...of

  - Utiliser for...of pour parcourir les valeurs du tableau.
  - Pas de var. Manipuler l’array correctement pour préfixer chaque valeur.

---

- Task 11 : Iterator – createEmployeesObject

  - Retourner { [departmentName]: employees }.

---

- Task 12 : Report object – createReportObject

  - Retourner { allEmployees: { ...employeesList }, getNumberOfDepartments(/*...`*`/) { ... } }.
  - La méthode reçoit l’objet (ou utilise this.allEmployees) et renvoie le nombre de départements (nombre de clés).
