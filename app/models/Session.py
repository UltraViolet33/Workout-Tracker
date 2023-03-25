from .. import db
from sqlalchemy.sql import func
from datetime import datetime


class Session_Exercises(db.Model):
    __tablename__ = "session_exercises"

    session_id = db.Column(db.Integer, db.ForeignKey(
        "sessions.id"), primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey(
        "exercises.id"), primary_key=True)
    
    series = db.Column("series", db.Integer)
    repetitions = db.Column("repetitons", db.Integer)


    session = db.relationship("Session", back_populates="exercises")
    exercise = db.relationship("Exercise", back_populates="sessions")


    def __init__(self, series, repetitions):
        self.series = series
        self.repetitions = repetitions
        


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date(), default=func.today(),
                     unique=True, nullable=False)

    # session_exercises = db.relationship("Exercise", secondary=sessions_list_exercises, backref="exercises")

    exercises = db.relationship("Session_Exercises", back_populates="session")

    def __init__(self):
        self.date = datetime.today()
