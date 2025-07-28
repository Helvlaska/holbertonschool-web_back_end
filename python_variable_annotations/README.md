# 📌 Python - Variable Annotations

Ce projet introduit les **annotations de type** en Python 3. Ces annotations permettent d’indiquer les types des variables, paramètres et retours de fonction. Elles facilitent la lecture du code, la détection d’erreurs avec `mypy`, et la robustesse générale des projets Python.

## 🎯 Objectifs pédagogiques

- Comprendre et utiliser les annotations de type en Python
- Annoter correctement les signatures de fonctions et variables
- Manipuler des types complexes avec `typing`
- Découvrir le duck typing et ses implications
- Vérifier statiquement le code avec `mypy`

## 🛠️ Technologies

- Python 3.9
- mypy
- Style: `pycodestyle` (v2.5)

## 📁 Contenu des fichiers

| Fichier | Fonction | Description |
|--------|----------|-------------|
| `0-add.py` | `add(a, b)` | Additionne deux floats |
| `1-concat.py` | `concat(str1, str2)` | Concatène deux chaînes |
| `2-floor.py` | `floor(n)` | Arrondi vers le bas un float |
| `3-to_str.py` | `to_str(n)` | Transforme un float en string |
| `4-define_variables.py` | Variables typées | Déclaration de variables annotées |
| `5-sum_list.py` | `sum_list(input_list)` | Somme d’une liste de float |
| `6-sum_mixed_list.py` | `sum_mixed_list(mxd_lst)` | Somme d'une liste de int/float |
| `7-to_kv.py` | `to_kv(k, v)` | Tuple `(k, v²)` où `v²` est un float |
| `8-make_multiplier.py` | `make_multiplier(multiplier)` | Retourne une fonction multiplicatrice |
| `9-element_length.py` | `element_length(lst)` | Retourne `(élément, longueur)` pour chaque élément d’une séquence |

## 🧪 Lancer les tests

```bash
python3 <n>-main.py
mypy <n>-*.py
```
