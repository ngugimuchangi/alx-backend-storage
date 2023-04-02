#!/usr/bin/env python3
"""
PyMongo operations: finding documents
"""


def list_all(mongo_collection):
    """
    Lists  all documents in a collection
    """
    return mongo_collection.find()
