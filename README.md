# 🚀 Flask + MySQL User API

A simple RESTful API built with **Python Flask** and **MySQL** to perform basic user operations:  
➕ Add user | 📄 Get user(s) | ❌ Delete user  

---

## 🌐 Live Demo

> 🧪 Test the API with [Postman](https://www.postman.com/)

---

## 📦 Features

- Add new users to a MySQL database
- Retrieve a list of all users
- Delete users by ID
- Clean and minimal code using Flask
- Easy to test with Postman

---

## 🛠️ Technologies Used

| Tech             | Purpose                  |
|------------------|---------------------------|
| Python 🐍        | Backend development       |
| Flask 🔥         | Micro web framework       |
| MySQL 🛢️        | Database                  |
| Postman 📬       | API testing               |
| VS Code 🧑‍💻     | Code editor               |

---

## ⚙️ Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/your-username/flask-mysql-api.git
cd flask-mysql-api
2. Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # On Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install flask mysql-connector-python
4. Setup MySQL
sql
Copy
Edit
CREATE DATABASE user_db;
USE user_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
5. Run the Flask App
bash
Copy
Edit
python app.py
🧪 API Endpoints
Method	Endpoint	Description
POST	/add_user	Add a new user
GET	/get_users	Get all users
DELETE	/delete_user/<id>	Delete user by ID
💡 Example JSON for Add User
json
Copy
Edit
{
  "name": "Ajith",
  "email": "ajith@gmail.com"
}
🙌 Acknowledgements
Special thanks to the mentors at Caze Labs Private Limited for the learning opportunity and guidance! 🙏

📌 Author
Ajith
Cloud Native Intern @ Caze Labs
LinkedIn

📜 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

📌 **Next Step**: Save this file as `README.md`, then:

```bash
git add README.md
git commit -m "Add README with project details"
git push