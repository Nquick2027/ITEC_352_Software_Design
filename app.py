from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate a database

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Create a GET request to retrieve all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# FET endpoint to fetch a user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
# POST endpoint to add new user
@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user["id"] = users[-1]["id"] + 1 if users else 1
    users.append(new_user)
    return jsonify(new_user), 201

# PUT endpoint to update a user's information
@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        update_data = request.get_json()
        user.update(update_data)
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
# DELETE endpoint to remove a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

# Need commands to run:
# Open terminal
# Split terminal
# Terminal 1: python app.py
# Terminal 2: curl http://127.0.0.1:5000/api/users