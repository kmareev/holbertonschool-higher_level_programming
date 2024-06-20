#!/usr/bin/python3
"""Creating a new Python file to import Flask """

# 1. Setting up Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

# 2. Creating my first Endpoint
@app.route('/')
def home():
    """Prints welcome message."""
    return "Welcome to the Flask API!"

# 3. Serving JSON Data
@app.route('/data')
def data():
    """Returns JSON data"""
    return jsonify(list(users.keys()))

# 4. Expanding my API
@app.route('/status')
def status():
    """ Returns the string OK """
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """ Returns corresponding info about a user """
    if username in users:
        return jsonify(users[username])
    return "User not found", 404

# 5. Handling POST Requests
@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the dictionary"""
    user_data = request.get_json()
    username = user_data.get('username')

    if not username:
        return "Username is required", 400

    if username in users:
        return "User already exists", 400
 
    users[username] = {
        'name' : user_data.get('name'),
        'age' : user_data.get('age'),
        'city' : user_data.get('city')
    }

    return jsonify({'message': 'User added successfully', 'user': users[username]}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001, debug=True)