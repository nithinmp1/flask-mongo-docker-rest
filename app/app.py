from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://my_mongo_db:27017/')
db = client['users']
collection = db['accounts']

@app.route("/", methods=["GET"])
def say_hello():
    return jsonify({"msg": "Welcome to cred"})

# Create operation
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    age = data.get('age')

    if not username or not email or not age:
        return jsonify({'error': 'Please provide username, email, and age'}), 400

    new_user = {
        'username': username,
        'email': email,
        'age': age
    }
    result = collection.insert_one(new_user)
    return jsonify({'message': 'User created successfully', 'id': str(result.inserted_id)}), 201

# Read operation
@app.route('/read', methods=['GET'])
def read():
    users = collection.find({}, {'_id': 0})
    return jsonify({'users': list(users)}), 200

# Update operation
@app.route('/update/<username>', methods=['PUT'])
def update(username):
    data = request.json
    new_email = data.get('email')
    new_age = data.get('age')

    if not new_email and not new_age:
        return jsonify({'error': 'Please provide email or age to update'}), 400

    query = {'username': username}
    new_values = {}
    if new_email:
        new_values['email'] = new_email
    if new_age:
        new_values['age'] = new_age

    result = collection.update_one(query, {'$set': new_values})
    if result.modified_count == 1:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

# Delete operation
@app.route('/delete/<username>', methods=['DELETE'])
def delete(username):
    query = {'username': username}
    result = collection.delete_one(query)
    if result.deleted_count == 1:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)