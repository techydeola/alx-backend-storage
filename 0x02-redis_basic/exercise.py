#!/usr/bin/env python3
"""
    a module for writing strings to redis
"""

import redis
import uuid
from typing import Union


class Cache:
    """
        a class that caches some data using redis instance
    """
    def __init__(self):
        """
            a function that initializes the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            a function that takes a data and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
