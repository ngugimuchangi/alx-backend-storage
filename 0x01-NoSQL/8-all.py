#!/usr/bin/env python3
"""
PyMongo operations: finding documents
"""


def list_all(mongo_collection):
    """
    Lists  all documents in a collection
    Return: cursor instance for documents found in the collection
    """
    return mongo_collection.find()
