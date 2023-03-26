from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])



class ExerciseForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    description = TextAreaField("description")
    category = SelectField(validators=[DataRequired()])


