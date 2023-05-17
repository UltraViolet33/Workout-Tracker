from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])


class ExerciseForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    description = TextAreaField("description")
    category = SelectField(validators=[DataRequired()])


class SessionForm(FlaskForm):
    exo = SelectField(validators=[DataRequired()])
    serie = IntegerField(validators=[DataRequired()])
    repetition = IntegerField(validators=[DataRequired()])
