import requests

url = "http://127.0.0.1:5000/add"

users = [
    {"name": "Ajith", "email": "ajith@gmail.com"},
    {"name": "Sneha", "email": "sneha123@gmail.com"},
    {"name": "Rahul Verma", "email": "rahulv23@example.com"},
    {"name": "Pooja Shetty", "email": "pooja.shetty@example.com"},
    {"name": "Nikhil Nair", "email": "nikhil.nair@gmail.com"},
    {"name": "Divya Rao", "email": "divya_rao@example.com"},
    {"name": "Ravi Kumar", "email": "ravi.kumar@example.com"},
    {"name": "Meera Fernandes", "email": "meera.fernandes@example.com"},
    {"name": "Harshad", "email": "harshad.tech@gmail.com"},
    {"name": "Anjali Patil", "email": "anjali.patil@gmail.com"}
]

for user in users:
    response = requests.post(url, json=user)
    print(f"Adding {user['name']} - Status Code: {response.status_code}, Response: {response.json()}")

