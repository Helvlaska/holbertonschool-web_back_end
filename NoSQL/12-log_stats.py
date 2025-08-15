#!/usr/bin/env python3
"""
Log stats:
- DB: logs
- Collection: nginx
- Affiche le nombre total de documents
- Puis, pour chaque méthode HTTP (GET, POST, PUT, PATCH, DELETE), le nombre d'occurrences
- Puis le nombre de documents avec method=GET et path=/status
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # total
    total = collection.count_documents({})
    print(f"{total} logs")

    # méthodes
    print("Methods:")
    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        n = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {n}")

    # statut
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
