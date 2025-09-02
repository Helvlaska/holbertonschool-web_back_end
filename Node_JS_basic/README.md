# NodeJS Basics

## 📖 Description

Ce projet introduit les bases de **Node.js** à travers une série de tâches progressives.
Il couvre l’exécution de scripts simples, la manipulation de fichiers, la gestion des arguments et entrées utilisateurs, ainsi que la mise en place de serveurs HTTP et Express, allant du plus minimaliste au plus structuré.

---

## 🎯 Objectifs pédagogiques

À la fin de ce projet, vous serez capable de :

- Exécuter du JavaScript avec NodeJS
- Utiliser les modules NodeJS
- Lire des fichiers en NodeJS (synchrone et asynchrone)
- Exploiter `process` pour récupérer les arguments et variables d’environnement
- Créer un petit serveur HTTP avec NodeJS
- Créer un serveur HTTP avec ExpressJS
- Mettre en place des routes avancées avec ExpressJS
- Utiliser **ES6 avec NodeJS** grâce à Babel-node
- Développer plus efficacement avec Nodemon

---

## 📂 Structure du projet

holbertonschool-web_back_end/
└── Node_JS_basic/
├── 0-console.js
├── 1-stdin.js
├── 2-read_file.js
├── 3-read_file_async.js
├── 4-http.js
├── 5-http.js
├── 6-http_express.js
├── 7-http_express.js
└── full_server/
├── utils.js
├── controllers/
│ ├── AppController.js
│ └── StudentsController.js
├── routes/
│ └── index.js
└── server.js

---

## ▶️ Installation & exécution

1. Installer les dépendances :

    ```bash
    npm install
    ```

2. Lancer un fichier :

    ```bash
    node 0-console.js
    ```

3. Exécuter le serveur Express (exemple avec full_server) :

    ```bash
    npm run dev
    ```

## ✅ Tests & Lint

Lancer les tests unitaires avec Jest :

```bash
npm run test
```

Vérifier lint + tests :

```bash
npm run full-test
```

---

## 📊 Contenu des tâches

0-console.js → Fonction displayMessage qui affiche une string en STDOUT

1-stdin.js → Programme interactif avec saisie utilisateur via stdin

2-read_file.js → Lecture synchrone d’un fichier CSV + statistiques étudiants

3-read_file_async.js → Lecture asynchrone d’un fichier CSV avec Promise

4-http.js → Petit serveur HTTP avec Node.js (http)

5-http.js → Serveur HTTP plus complexe avec route /students

6-http_express.js → Serveur HTTP basique avec ExpressJS

7-http_express.js → Serveur Express avec route /students

full_server/ → Organisation complète (controllers, routes, utils) + gestion avancée des étudiants
