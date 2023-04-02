#!/usr/bin/env python3
"""
PyMongo operations: finding documents
"""
from pymongo.collection import Collection
from pymongo.cursor import Cursor


def list_all(mongo_collection: Collection) -> Cursor:
    """
    Lists  all documents in a collection
    Return: cursor instance for documents found in the collection
    """
    return mongo_collection.find()
