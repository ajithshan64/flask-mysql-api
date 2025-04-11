from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection config
db = mysql.connector.connect(
    host="localhost",
    user="root",         # change this if your MySQL username is different
    password="",         # put your MySQL password here (default is empty for XAMPP)
    database="user_db"
)

cursor = db.cursor()

# 🧩 Route: Add a user
@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']

    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        db.commit()
        return jsonify({'message': 'User added successfully'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400

# 📋 Route: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    users = [{'id': row[0], 'name': row[1], 'email': row[2]} for row in result]
    return jsonify(users)

# ❌ Route: Delete user by ID
@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    db.commit()
    return jsonify({'message': 'User deleted successfully'})

# 🚀 Run the app
if __name__ == '__main__':
    app.run(debug=True)
