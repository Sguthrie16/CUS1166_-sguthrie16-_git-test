from flask import Flask, render_template, url_for, flash, redirect
from forms import Register, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
user=[
{
'name': 'Sarah',
'user_id': '123',
'model': 'truck',
},
{
'name': 'Shawns',
'user_id':'456',
'model':'mini van',
}
]
@app.route("/")
def user():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
