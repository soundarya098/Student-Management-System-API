from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from models import db, bcrypt, User, Student
from schema import ma, student_schema, students_schema
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)

# Create tables
with app.app_context():
    db.create_all()

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.username)
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

# Add Student
@app.route('/students', methods=['POST'])
@jwt_required()
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'], course=data['course'])
    db.session.add(new_student)
    db.session.commit()
    return student_schema.jsonify(new_student), 201

# Get All Students
@app.route('/students', methods=['GET'])
@jwt_required()
def get_students():
    all_students = Student.query.all()
    return students_schema.jsonify(all_students)

# Update Student
@app.route('/students/<int:id>', methods=['PUT'])
@jwt_required()
def update_student(id):
    student = Student.query.get(id)
    data = request.get_json()
    student.name = data['name']
    student.age = data['age']
    student.course = data['course']
    db.session.commit()
    return student_schema.jsonify(student)

# Delete Student
@app.route('/students/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
