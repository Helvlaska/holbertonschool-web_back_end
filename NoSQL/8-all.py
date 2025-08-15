#!/usr/bin/env python3
"""Liste tout les documents d'une collection MongoDB """


def list_all(mongo_collection):
    """Retourne tout les documents de la collection comme une liste.
    Si la collection vaut None ou vide, retourne une liste vide """
    if mongo_collection is None:
        return []

    cursor = mongo_collection.find()
    documents = list(cursor)
    return documents
