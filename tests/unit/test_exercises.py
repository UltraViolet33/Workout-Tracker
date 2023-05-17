from app import db
from app.models.Exercise import Exercise
from app.models.Category import Category


def test_get_all_exos(test_client, init_database):
    category = Category.query.filter_by(name="category1").first()
    exo1 = Exercise(name="Test Exercise 1",
                    description="Test Description 1", category=category)
    exo2 = Exercise(name="Test Exercise 2",
                    description="Test Description 2", category=category)
    db.session.add_all([exo1, exo2])
    db.session.commit()

    response = test_client.get("/exos/all")

    assert response.status_code == 200

    assert exo1.name in str(response.data)
    assert exo2.name in str(response.data)
