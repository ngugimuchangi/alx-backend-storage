#!/usr/bin/env python3
"""
Aggregation operations
"""
from pymongo import MongoClient
from collections import OrderedDict


def get_nginx_stats():
    """
    Queries nginx collection for specific data
    Return:
        - count of all documents
        - count of each method in the collection
        - count of each GET calls to /status path
    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    pipeline = [{'$match': {'method': {'$in': methods}}},
                {'$group': {'_id': '$method', 'count': {'$sum': 1}}},
                {'$sort': OrderedDict([('count', -1), ('_id', -1)])}]
    count = collection.estimated_document_count()
    method_stats = collection.aggregate(pipeline)
    status_path_stats = collection.count_documents({'method': 'GET',
                                                    'path': '/status'})
    client.close()
    return count, method_stats, status_path_stats


def print_nginx_stats():
    """
    Prints stats from nginx query
    """
    count, method_stats, status_path_stats = get_nginx_stats()
    print(f'{count} logs')
    print('Methods:')
    for method in method_stats:
        print(f'\tmethod {method.get("_id")}: {method.get("count")}')
    print(f'{status_path_stats} status check')


if __name__ == '__main__':
    print_nginx_stats()
