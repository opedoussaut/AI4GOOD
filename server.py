import os
from pymongo import MongoClient
from flask import Flask, jsonify, request

app = Flask(__name__)

mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_uri = f"mongodb+srv://{mongo_user}:{mongo_password}@ecoinventdb.zss85ou.mongodb.net/"
client = MongoClient(mongo_uri)
db = client["ecoinventDB"]
collection = db["cutoff_activities"]

@app.route('/activities', methods=['GET'])
def get_activities():
    query = {}
    result = list(collection.find(query).limit(10))
    for doc in result:
        doc['_id'] = str(doc['_id'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)