<<<<<<< HEAD
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
=======
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
>>>>>>> de8368feb7cd6f2348eda3ba94eb50b425ef5f26
