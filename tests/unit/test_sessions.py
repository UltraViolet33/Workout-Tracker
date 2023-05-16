from flask import url_for
from app import create_app, db
from app.models.Session import Session
from app.models.Exercise import Exercise
from app.models.Category import Category
from app.models.Session import Session_Exercises
from datetime import datetime


def test_route_all_sessions(test_client, init_database):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"All Sessions" in response.data


def test_get_session_details(test_client, init_database):
    session = Session()
    db.session.add(session)
    db.session.commit()

    response = test_client.get(f"/sessions/details/{session.id}")

    assert response.status_code == 200
    assert session.date.strftime("%Y-%m-%d") in str(response.data)



def test_create_session(test_client, init_database):
    category = Category.query.filter_by(name="category1").first()
    exercise = Exercise(name="Test Exercise", description="desc", category=category)
    db.session.add(exercise)
    db.session.commit()

    response = test_client.post("/sessions/create", data={
        "exo": exercise.id,
        "repetition": 10,
        "serie": 5
    })

    assert response.status_code == 200
    assert b"Exo added to session" in response.data

    session_exercise = Session_Exercises.query.filter_by(
        exercise_id=exercise.id,
        repetitions=10,
        series=5
    ).first()
    assert session_exercise is not None