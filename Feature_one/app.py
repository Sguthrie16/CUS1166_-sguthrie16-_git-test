from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', Car=Car)

@app.route("/userlist")
def user():
    return render_template('user.html', User=User)
