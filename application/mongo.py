from pymongo import MongoClient


def get_client():
    client = MongoClient(host='interview_mongodb',
                         port=27017,
                         username='root',
                         password='pass',
                         authSource="admin")
    return client
