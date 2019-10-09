import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():

    courses = db.execute("SELECT * from courses")
    return render_template('index.html', courses=courses)



@app.route("/add_course",methods=["post"])
def add_course():

    id = request.form.get("id")
    number = request.form.get("number")
    title = request.form.get("title")

    courses =db.execute("INSERT INTO courses (id,number,title) VALUES (:id, :number, :title)"
    {"id": id,"number": number,"title" : title})
    db.commit()
    Course = db.execute("SELECT * from courses")

    return render_template('index.html',courses=courses)



@app.route("/register_student/int:course_id", methods=["GET", "POST"])
def register_student(student_id):

    student = Course.query.get(student_id)

    if request.method == 'POST':
        name = request.form.get("name")
        grade = request.form.get("grade")
        student.add_student(name,grade)
    students = student.students
    return render_template("course_details.html", student=student, students=students)
def main():
    if (len(sys.argv)==2):
        print(sys.argv)
        if sys.argv[1] == 'createdb':
            db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'python app.py createdb")
# Run the main method in the context of our flass application
# This allows db know about our models.
if __name__ == "__main__":
    with app.app_context():
        main()
