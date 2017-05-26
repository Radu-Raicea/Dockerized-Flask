from project import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Numbercol(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    numbercol = db.Column(db.Integer)

    def __init__(self, numbercol):
        self.numbercol = numbercol


db.create_all()
db.session.commit()
