from pymongo import MongoClient
import pprint
import json
from bson.json_util import dumps, loads
client = MongoClient("jersey.optonline.net", 27017)

mydatabase = client.inventory
mycollection = mydatabase.servers

cursor = mycollection.find()

list_cur = list(cursor)
json_data = dumps(list_cur, indent=2)
print(json_data)
