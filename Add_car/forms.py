from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class AddCarForm(Form):    ## username= StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    user_id = StringField('Name', validators= [DataRequired()])
    make = StringField('Make', validators= [DataRequired()])
    model = StringField('Model', validators= [DataRequired()])
    color = StringField('Color', validators= [DataRequired()])
    car_vin = StringField('Car VIN', validators= [DataRequired()])
    submit = SubmitField('Add Car')
