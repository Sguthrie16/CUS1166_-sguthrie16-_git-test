from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Car(db.Model):
    __tablename__ = 'Car'
    car_vin = db.Column(db.String(17),  primary_key=True)
    Model = db.Column(db.String(20), nullable = False)
    Make = db.Column(db.String(20), nullable = False)
    Color = db.Column(db.String(20), nullable = False)
    user_id = db.Column(db.Integer, nullable=False)
        
    def __repr__(self):
        return '<Car {}>'.format(self.user_id)
