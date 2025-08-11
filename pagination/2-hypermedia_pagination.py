#!/usr/bin/env python3
"""Pagination hypermedia sur un dataset CSV.

Expose Server.get_hyper() qui renvoie une page de données et ses métadonnées
(page_size effectif, page, data, next_page, prev_page, total_pages).
Repose sur get_page() pour le découpage.
"""
import csv
import math
from typing import Dict, Tuple, List, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retourne (start, end) pour une page 1-indexée ; end est exclusif."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """La classe Server pagine les noms de bébés populaire"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Charge et met en cache le dataset (en-tête exclue)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Renvoyer la 'page' demandée du dataset.
        - Valide que page et page_size sont des int > 0 (assert).
        - Calcule (start, end) via index_range.
        - Retourne data[start:end] (liste vide si hors bornes).
        """
        # Récupère la liste des éléments du fichier csv
        data = self.dataset()

        # Vérifie que page et page_size sont des int > 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Récupère l'index de départ et l'index de fin
        start, end = index_range(page, page_size)

        # Renvoie les données entre start et end
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Retourne une page et ses métadonnées de navigation.

        Inclut page_size effectif, page, data, next_page, prev_page
        et total_pages.
        Réutilise get_page() pour obtenir la tranche de données.
        """
        # Récupère le nombre total de lignes dans le fichier
        total = len(self.dataset())

        # Vérifie si le nb total de ligne est > 0
        # Si oui on divise le nb de ligne par la taille des pages = nb pages
        # Sinon le nb de pages = 0
        if total > 0:
            total_pages = math.ceil(total / page_size)
        else:
            total_pages = 0

        # Récupère la page demandée
        data_page = self.get_page(page, page_size)

        # Vérifie s'il y a une page suivante
        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        # Vérifie s'il y a une page précédante
        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        # Retourne le dictionnaire avec les informations
        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
