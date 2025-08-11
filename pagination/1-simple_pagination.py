#!/usr/bin/env python3
"""Utilitaire de pagination : retourne (start, end) pour une page."""
import csv
from typing import Tuple, List


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
