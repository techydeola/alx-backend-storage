#!/usr/bin/env python3
"""
    a Python module for task 10 of NoSQL project
"""


def update_topics(mongo_collection, name, topics):
    """
        a function that changes all topics of a school document
        based on the name

        Return: id
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
