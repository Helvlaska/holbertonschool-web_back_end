#!/usr/bin/env python3
"""Renvoie une liste d'école qui on un champ topics spécifique"""


def schools_by_topic(mongo_collection, topic):
    """Retourne une liste vide si la collection est vide ou None.
    Sinon retourne une liste de documents"""
    if mongo_collection is None or not isinstance(topic, str):
        return []

    cursor = mongo_collection.find({"topics": topic})
    docs = list(cursor)          # matérialise le curseur en liste
    return docs
