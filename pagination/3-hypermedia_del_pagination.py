#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
from typing import Dict, List, Optional, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        # Récupère ligne par ligne les données du fichier csv
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    # Fonction pour créer un dictionnaire cle(index): value(ligne)
    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    # Fonction pour retourner un dictionnaire avec différentes informations
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retourne une page à partir d'un index, robuste aux suppressions.

        Renvoie un dict :
          - index: index de départ demandé (tel quel)
          - next_index: index pour la requête suivante (ou None en fin)
          - page_size: taille effective renvoyée
          - data: la page de lignes
        """
        # Vérifie que index = None + initialise à 0
        if index is None:
            index = 0

        # Récupère les lignes du document csv
        indexed = self.indexed_dataset()

        # Vérification des types des arguments passés à la fonction
        if not isinstance(index, int):
            raise AssertionError
        if not isinstance(page_size, int) or page_size <= 0:
            raise AssertionError

        # Vérification si la page est vide
        if len(indexed) == 0:
            # Création d'un dictionnaire vide
            result = {}

            # Informations à ajouter dans le dictionnaire
            result["index"] = index
            result["next_index"] = None
            result["page_size"] = 0
            result["data"] = []         # Pas de lignes à renvoyer → liste vide

            return result               # On return le dictionnaire

        # Détermine le dernier index du fichier csv
        max_key = max(indexed.keys())

        # Vérifie que l'index est bien entre le début et la fin du fichier csv
        assert 0 <= index <= max_key

        # Data est une liste de listes de lignes (vide pour le moment)
        data: List[List] = []
        # Current est un curseur de lecture (démarre à l'index demandé)
        current: int = index
        # Max_key est le dernier index du fichier csv
        max_key: int = max(indexed.keys())

        # Boucle pour récupérer les informations
        while True:                           # Tant que la condition est vraie
            # Vérifie si la taille de liste est >= au nb d'éléments de la page
            if len(data) >= page_size:
                break

            # Vérifie si on ne dépasse pas l'index final
            if current > max_key:
                break

            # Vérifie si l'index current est vide ou sinon l'ajoute
            if current in indexed:
                row = indexed[current]
                data.append(row)

            # On avance dans les index
            current = current + 1

        # Vérifie si il reste des lignes, le current devient le next_index
        if current <= max_key:
            next_index: Optional[int] = current
        else:
            next_index = None

        # Détermine la taille de la page (page_size)
        effective_size: int = len(data)

        # Construction de la réponse
        result: Dict[str, Any] = {}
        result["index"] = index
        result["data"] = data
        result["page_size"] = effective_size
        result["next_index"] = next_index

        return result
