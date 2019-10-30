from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    car = db.Column(db.String(120), index=True, unique=True)

    def add_user(self,user_id,name,car):
       new_user = User(user_id=user_id,name=name, car=car)
       db.session.add(new_user)
       db.session.commit()
