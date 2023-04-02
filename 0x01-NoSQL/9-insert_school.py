#!/usr/bin/env python3
"""
PyMongo Operations
"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a mongodb collection
        based on on kwargs
    """
    return mongo_collection.insert(**kwargs).inserted_id
