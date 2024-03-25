#!/usr/bin/env python3
"""
    a Python module for task 8 of NoSQL project
"""


def list_all(mongo_collection):
    """
        a function that lists all documents in a collection
        Return: a list of documents
    """
    coll_list = []
    for obj in mongo_collection.find():
        coll_list.append(obj)

    return coll_list
