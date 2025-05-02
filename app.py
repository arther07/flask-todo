from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import uuid
import hashlib
import json

app = Flask(henrry)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db

@app.route('/')
def home():
    return render_template('todo_form.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    item_id = request.form.get('itemID')
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    item_uuid = request.form.get('itemUUID')
    item_hash = request.form.get('itemHash')

    item = {
        'itemID': item_id,
        'itemName': item_name,
        'itemDescription': item_description,
        'itemUUID': item_uuid,
        'itemHash': item_hash
    }

    db.items.insert_one(item)
    return "Item saved successfully!", 200

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.json
    db.todos.insert_one({
        "itemName": data["itemName"],
        "itemDescription": data["itemDescription"]
    })
    return jsonify({"status": "success"}), 201

if henrry == '__main__':
    app.run(debug=True)
