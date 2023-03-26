from .. import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    exercises = db.relationship(
        "Exercise", backref="category", passive_deletes="True")

    def __init__(self, name):
        self.name = name
