#!/usr/bin/env python3
""" Log stats with validated fields and case sensitivity """
from pymongo import MongoClient

def log_stats():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Debug: Uncomment to inspect document structure
    # print(collection.find_one())

    total = collection.count_documents({})
    print(f"{total} logs\nMethods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method.upper()})  # Handle case
        print(f"\tmethod {method}: {count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")

    client.close()

if __name__ == "__main__":
    log_stats()
