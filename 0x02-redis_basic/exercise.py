#!/usr/bin/env python3
""" Redis client module
"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """ Decorator for Cache class methods
    """
    @wraps(method)
    def wrapper(self: Any, data: Union[str, bytes,  int,  float]) -> Callable:
        """ Wraps called method and adds its call count redis before execution
        """
        self._redis.incr(method.__qualname__)
        return method(self, data)
    return wrapper


class Cache:
    """ Caching class
    """
    def __init__(self) -> None:
        """ Initialize new cache object
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        """ Stores data in redis with randomly generated key
        """
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """ Gets key's value from redis and converts
            result byte  into correct data type
        """
        client = self._redis
        value = client.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to integers
        """
        return int(data)
