from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    
    if not item_name or not item_description:
        return jsonify({'status': 'fail', 'reason': 'Missing fields'}), 400

    collection.insert_one({
        'itemName': item_name,
        'itemDescription': item_description
    })
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)

