#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from typing import Callable

client = redis.Redis()


def get_cache(fn: Callable) -> Callable:
    """ Decorator for get_page
    """
    def wrapper(url: str) -> str:
        """ Wrapper that:
            - check whether a url's data is cached
            - tracks how many times get_page is called
        """
        client.incr(f'count:{url}')
        cached_page = client.get(url)
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        # client.set(f'count:{url}', 0)
        client.setex(url, 10, response)
        return response
    return wrapper


@get_cache
def get_page(url: str) -> str:
    """ Makes a http request to a given endpoint
    """
    response = requests.get(url)
    return response.text
