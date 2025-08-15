#!/usr/bin/env python3
"""Remplace le champ 'topics' pour toutes les écoles"""


def update_topics(mongo_collection, name, topics):
    """Renvoie les topics pour tout les documents dont name == <name>"""
    mongo_collection.update_many(
        {"name": name},   # Filtre tout les documents qui on un attribut 'name'
        {"$set": {"topics": topics}}  # Ajout du nouveau champ 'topics'
    )
