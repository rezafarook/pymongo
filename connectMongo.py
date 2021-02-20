from pymongo import MongoClient
import pprint
import json
client = MongoClient("jersey.optonline.net", 27017)

mydb = client["inventory"]
mycol = mydb["servers"]

#answer = mycol.find({'make': 'HP'})
#print(answer)

# for value in mycol.find({'make': 'HP'}):
#     pprint.pprint(value)

theval = mycol.find({'make': 'HP'})
list_cur = list(theval)
json_data = json.dumps(list_cur, indent=2)
print(json_data)



#for db in client.list_databases():
