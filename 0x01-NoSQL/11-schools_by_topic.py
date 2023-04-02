#!/usr/bin/env python3
"""
PyMongo operations: matching data in list
"""
from pymongo.collection import Collection
from pymongo.cursor import Cursor


def schools_by_topic(mongo_collection: Collection, topic: str) -> Cursor:
    """
    Finds a list of school having a specific topic
    """
    return mongo_collection.find({'topics': topic})
