#!/usr/bin/env python3
"""
    a Python module for task 10 of NoSQL project
"""


def schools_by_topic(mongo_collection, topic):
    """
        that returns the list of school having a specific topic

        Return: a list
    """
    schoolList = []
    datas = mongo_collection.find({"topics": topic})
    for data in datas:
        schoolList.append(data)

    return schoolList
