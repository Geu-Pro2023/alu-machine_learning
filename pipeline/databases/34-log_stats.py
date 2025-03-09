#!/usr/bin/env python3
""" Log stats with exact output formatting """
from pymongo import MongoClient


def log_stats():
    """ Provides stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total logs count
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check count
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    client.close()


if __name__ == "__main__":
    log_stats()
