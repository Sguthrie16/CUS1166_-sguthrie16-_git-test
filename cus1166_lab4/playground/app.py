from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome_student_name(student_name):
    return render_template("welcome.html",student_name=student_name)


@app.route("/roster/<int:grade_view>")
def roster_grade_view(grade_view):
    student1=("Sarah","A","Junior")
    student2=("Shawn","B+","Senior")
    student3=("Sam","B","Sophmore")
    student4=("Max","B-","Junior")
    student5=("Jackie","A+","Freshman")
    student6=("Dee","C","Sophmore")
    student7=("John","C+","Junior")

    class_roster=[student1,student2,student3,student4,student5,student6,student7]
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == '__main__':
	app.run(debug=True)
