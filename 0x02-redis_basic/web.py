#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from typing import Callable


def call_count(fn: Callable) -> Callable:
    """ Decorator for get_page
    """
    def wrapper(*args, **kwargs) -> str:
        """ Wrapper that:
            - check whether a page is cached
            - tracks how many times get_page is called
        """
        url = args[0]
        client = redis.Redis()
        cached_page = client.get(url)
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(*args, **kwargs)
        client.incr(f'count:{url}')
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@call_count
def get_page(url: str) -> str:
    """ Makes a http request to a given endpoint
    """
    response = requests.get(url)
    return response.text
