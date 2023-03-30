#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from typing import Callable
from functools import wraps


def track_get_page(fn: Callable) -> Callable:
    """ Decorator for get_page
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """ Wrapper that:
            - check whether a url's data is cached
            - tracks how many times get_page is called
        """
        client = redis.Redis()
        cached_data = client.get(f'cached:{url}')
        if cached_data:
            return cached_data.decode('utf-8')
        response = fn(url)
        client.incr(f'count:{url}')
        client.setex(f'cached{url}', 10, response)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """ Makes a http request to a given endpoint
    """
    response = requests.get(url)
    return response.text
