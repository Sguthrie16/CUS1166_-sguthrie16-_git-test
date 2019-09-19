from flask import Flask, render_template
app= Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html",student_name=student_name)


@app.route("/roster/<int:grade_view>")
def welcome(grade_view):
class_roster=[("John","A","Freshman"),("Tom","B","Senior")]
    return render_template("roster.html",class_roster=class_roster, grade_view=grade_view)
