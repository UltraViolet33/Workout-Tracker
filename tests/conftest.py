import pytest
from app import create_app, db
from app.models.Category import Category


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app("config.TestingConfig")

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope="module")
def init_database(test_client):
    db.create_all()

    category = Category(name="category1")

    db.session.add(category)
    db.session.commit()

    yield

    db.drop_all()