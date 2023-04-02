#!/usr/bin/env python3
"""
Aggregation operations: average
"""
from collections import OrderedDict
from pymongo.collection import Collection


def top_students(mongo_collection: Collection):
    """
    Gets list of students from mongo collection
    and returns the list of computed average for
    each student
    """
    pipeline = [{'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
                {'$sort': OrderedDict([('averageScore', -1), ('name', 1)])}]
    return mongo_collection.aggregate(pipeline)
