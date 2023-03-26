from flask import Blueprint, request, render_template, redirect, url_for, request, flash
from . import db
from .models.Category import Category
from .models.Exercise import Exercise
from .models.Session import Session
from .models.Session import Session_Exercises
from sqlalchemy.sql.expression import func
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired
from datetime import datetime



sessions = Blueprint("sessions", __name__)


class SessionForm(FlaskForm):    
    exo = SelectField(validators=[DataRequired()])
    serie = IntegerField(validators=[DataRequired()])
    repetition = IntegerField(validators=[DataRequired()])



@sessions.route("/", methods=["GET"])
def all_session():
    
    all_sessions = Session.query.all()
    
    return render_template("allSessions.html", sessions=all_sessions)






@sessions.route("/sessions/details/<id>", methods=["GET"])
def get_session_details(id):

    session = Session.query.filter_by(id=id).first()  

    for exo in session.exercises:
        print(exo)  

    return render_template("detailsSession.html", session=session)




@sessions.route("/sessions/create", methods=["GET", "POST"])
def create_session():

    form = SessionForm()
    form.exo.choices = [(e.id, e.name) for e in Exercise.query.all()]

    print(datetime.today())
    if form.validate_on_submit():
        
        session = Session.query.filter_by(date=datetime.today().strftime('%Y-%m-%d')).first()

        print(session)

        if not session:
            session = Session()
            db.session.add(session)
            db.session.commit()

        exo = Exercise.query.filter_by(id=form.exo.data).first()

        session_exo = Session_Exercises.query.filter(Session_Exercises.session_id==session.id, Session_Exercises.exercise_id==exo.id, Session_Exercises.repetitions == form.repetition.data).first()

        if session_exo:
            print("ok")
            session_exo.series += form.serie.data
            db.session.commit()

        else:


            session_exo = Session_Exercises(series=form.serie.data, repetitions=form.repetition.data)
            session_exo.exercise = exo 
            session.exercises.append(session_exo)

            db.session.add(session_exo)
            db.session.commit()

        # print(exo)


    return render_template("formSession.html", form=form)



    # get all exos
    # display select fields with all exos
    # display nb series and nb repetitions

    # check if the session already exists
    # check if the repetiton exists already for this sessions and this exo
    # update or create
    # display all the exos on the page
    