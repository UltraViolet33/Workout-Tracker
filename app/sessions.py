from flask import Blueprint, request, render_template, redirect, url_for, request, flash
from . import db
from .models.Category import Category
from .models.Exercise import Exercise
from .models.Session import Session

from sqlalchemy.sql.expression import func
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


sessions = Blueprint("sessions", __name__)


# class ExerciseForm(FlaskForm):
#     name = StringField("name", validators=[DataRequired()])
#     description = TextAreaField("description")
#     category = SelectField(validators=[DataRequired()])



@sessions.route("/", methods=["GET"])
def create_session():
    pass 



@sessions.route("/sessions/create", methods=["GET", "POST"])
def create_session():
    # get all exos
    # check if the session already exists
    # display select fields with all exos
    # display nb series and nb repetitions
    # check if the repetiton exists already for this sessions and this exo
    # update or create
    # display all the exos on the page
    pass 