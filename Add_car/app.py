from flask import Flask, render_template
from config import Config
from forms import *
from models import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    form= AddCarForm()
    if form.submit():
        db.create_all()
        car = Car(user_id=form.user_id.data, car_vin=form.car_vin.data)
        db.session.add(car)
        db.session.commit()
        flash('Congratulations, you registered a car!')
    return render_template('add_car.html', title='Add car', form=form)

if __name__ == '__main__':
    app.run(debug=True)
