from flask import Blueprint, request, render_template, redirect, url_for, request, flash
from . import db
from .models.Category import Category
from .models.Exercise import Exercise
from .models.Session import Session

from sqlalchemy.sql.expression import func
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired


sessions = Blueprint("sessions", __name__)


class SessionForm(FlaskForm):
    
    exo = SelectField(validators=[DataRequired()])
    serie = IntegerField(validators=[DataRequired()])
    repetition = IntegerField(validators=[DataRequired()])



# @sessions.route("/", methods=["GET"])
# def all_session():
#     pass 



@sessions.route("/sessions/create", methods=["GET", "POST"])
def create_session():

    form = SessionForm()
    form.exo.choices = [(e.id, e.name) for e in Exercise.query.all()]


    return render_template("formSession.html", form=form)



    # get all exos
    # check if the session already exists
    # display select fields with all exos
    # display nb series and nb repetitions
    # check if the repetiton exists already for this sessions and this exo
    # update or create
    # display all the exos on the page
    