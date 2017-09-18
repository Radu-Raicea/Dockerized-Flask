
from project import db
from flask_sqlalchemy import SQLAlchemy


class Numbercol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numbercol = db.Column(db.Integer)

    def __init__(self, numbercol):
        self.numbercol = numbercol

    def __repr__(self):
        return '<Numbercol Object %r>' % self.id
