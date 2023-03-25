from .. import db


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.Integer, db.ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)


    sessions = db.relationship("Session_Exercises", back_populates="exercise")


    def __init__(self, name, description, category):
        self.name = name
        self.description=description
        self.category = category
