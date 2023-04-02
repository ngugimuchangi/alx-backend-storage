#!/usr/bin/env python3
"""
PyMongo operations: updating documents
"""
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection,
                  name: str, topics: str) -> None:
    """
    Updates topics field with given topics for
    documents whose name field matches given name
    """
    mongo_collection.update_many({'name': name},
                                 {'$set': {'topics': topics}})
