from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
   # Map this model to a flights table
   __tablename__= "courses"
   # Specify the columns/ fields of the model.
   id = db.Column(db.String, nullable = False)
   course_number = db.Column(db.String, nullable = False)
   cour_title = db.Column(db.String, nullable = False)

   # Specify any relationship fields.
   students = db.relationship("Student", backref="flights", lazy=True)
   # specify any utility methods associated with the model.
   def add_student(self,id,name,grade):
       # Notice that we set the foreign key for the passenger class.
       new_student = Student(id=id,name=name, grade=grade)
       db.session.add(new_student)
       db.session.commit()
#Define a Passenger model.
class RegisteredStudent(db.Model):
   __tablename__ = "registeredstudents"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable = False)
   grade = db.Column(db.Integer, primary_key=True)
   # Notice, this field serves as a foreighKey.
   student_id = db.Column(db.Integer, db.ForeignKey('registeredstudents.id'), nullable=False)
