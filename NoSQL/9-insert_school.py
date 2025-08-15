#!/usr/bin/env python3
"""Création d'un nouveau document dans une collection MongoDB"""


def insert_school(mongo_collection, **kwargs):
    """Insert un nouveau document dans une collection via les kwargs"""
    result = mongo_collection.insert_one(dict(kwargs))
    return result.inserted_id
