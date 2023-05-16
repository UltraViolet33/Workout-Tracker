from flask import Blueprint, render_template, flash, request
from . import db
from .models.Exercise import Exercise
from .models.Session import Session
from .models.Session import Session_Exercises
from datetime import datetime
from .forms import SessionForm


sessions = Blueprint("sessions", __name__)


@sessions.route("/", methods=["GET"])
def all_session():
    all_sessions = Session.query.all()
    return render_template("allSessions.html", sessions=all_sessions)


@sessions.route("/sessions/details/<id>", methods=["GET"])
def get_session_details(id):
    session = Session.query.filter_by(id=id).first()
    return render_template("detailsSession.html", session=session)


@sessions.route("/sessions/create", methods=["GET", "POST"])
def create_session():
    form = SessionForm()
    form.exo.choices = [(e.id, e.name) for e in Exercise.query.all()]

    if form.validate_on_submit() or request.form.get("exo"):

        session = Session.query.filter_by(
            date=datetime.today().strftime('%Y-%m-%d')).first()

        if not session:
            session = Session()
            db.session.add(session)
            db.session.commit()

        exo = Exercise.query.filter_by(id=form.exo.data).first()
        session_exo = Session_Exercises.query.filter(
            Session_Exercises.session_id == session.id, Session_Exercises.exercise_id == exo.id, Session_Exercises.repetitions == form.repetition.data).first()

        if session_exo:
            session_exo.series += form.serie.data
            db.session.commit()
        else:
            session_exo = Session_Exercises(
                series=form.serie.data, repetitions=form.repetition.data)
            session_exo.exercise = exo
            session.exercises.append(session_exo)
            db.session.add(session_exo)
            db.session.commit()

        flash("Exo added to session")

    return render_template("formSession.html", form=form, today=datetime.today().strftime('%Y-%m-%d'))

