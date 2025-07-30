## Student-Management-System-API

## 📌 Description
A secure backend API for managing student records with authentication and CRUD operations. Built with Flask and SQLite.

## 🚀 Features
- User registration and login with password hashing
- JWT authentication for secure API access
- CRUD operations for student records
- SQLite database with SQLAlchemy ORM
- Tested with Postman

## 🛠 Tech Stack
- Python
- Flask
- SQLite
- SQLAlchemy
- Flask-Bcrypt
- Flask-JWT-Extended
- Postman


## 📌 API Endpoints
- POST /register – Register a new user
- POST /login – Login and get token
- POST /students – Add student (JWT required)
- GET /students – Get all students (JWT required)
- PUT /students/<id> – Update student by ID (JWT required)
- DELETE /students/<id> – Delete student by ID (JWT required)

## ▶ How to Run
```bash
pip install -r requirements.txt
python app.py

## The API will start at:
http://127.0.0.1:5000/
