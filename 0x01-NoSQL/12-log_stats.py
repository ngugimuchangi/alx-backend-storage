#!/usr/bin/env python3
"""
Aggregation operations
"""
from pymongo import MongoClient


def sorting_func(method_dict):
    """
    Returns tuple of elements to use for sorting
    in the right order
    """
    dict_items = list(method_dict.items())
    return (dict_items[1], dict_items[0])


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
    method_stats = []
    for method in methods:
        count = collection.count_documents({'method': method})
        method_stats.append({'method': method, 'count': count})
    method_stats.sort(key=sorting_func, reverse=True)
    count = collection.estimated_document_count()
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
        print(f'\tmethod {method.get("method")}: {method.get("count")}')
    print(f'{status_path_stats} status check')


if __name__ == '__main__':
    print_nginx_stats()
