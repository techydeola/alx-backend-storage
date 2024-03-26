#!/usr/bin/env python3
"""
    a Python module for task 9 of NoSQL project
"""


def insert_school(mongo_collection, **kwargs):
    """
        a function that inserts a new document in a collection
        Return: nothing
    """
    data = {key: value for key, value in kwargs.items()}
    result = mongo_collection.insert_one(data)

    return result.inserted_id
