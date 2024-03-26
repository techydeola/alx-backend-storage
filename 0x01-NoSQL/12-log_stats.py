#!/usr/bin/env python3
"""
    a Python script that provides some stats about Nginx
    logs stored in MongoDB:
"""

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient(host="localhost", port=27017)
    db = client["logs"]
    collection = db.nginx

    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    status = collection.count_documents({"path": "/status"})

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
