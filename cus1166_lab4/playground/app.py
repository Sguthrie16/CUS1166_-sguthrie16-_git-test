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
    name=("Sarah","Shawn","Mark","Terrence","John","Max","Mary")
    year=("Junior", "Senior","Freshman","Sophmore","Freshman","Senior","Junior")
    grade=("A","B","A-","B+","C","A","B-")
    class_roster=[name,grade,year]
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == '__main__':
	app.run(debug=True)