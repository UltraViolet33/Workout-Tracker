from app import db
from app.models.Exercise import Exercise
from app.models.Category import Category


def test_get_all_categories(test_client, init_database):
    category1 = Category(name="Test Category 1")
    category2 = Category(name="Test Category 2")
    db.session.add_all([category1, category2])
    db.session.commit()

    response = test_client.get("/categories/all")

    assert response.status_code == 200

    assert category1.name in str(response.data)
    assert category2.name in str(response.data)


def test_get_exos_category(test_client, init_database):
    category = Category(name="Test Category")
    exercise = Exercise(name="Test Exercise",
                        description="desc", category=category)
    db.session.add_all([category, exercise])
    db.session.commit()

    response = test_client.get(f"/categories/{category.id}")

    assert response.status_code == 200

    assert category.name in str(response.data)
    for exercise in category.exercises:
        assert exercise.name in str(response.data)
