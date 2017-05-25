from project import db

class Numbercol(db.Model):
	uid = db.Column(db.Integer, primary_key=True)
	numbercol = db.Column(db.Integer)

	def __init__(self, numbercol):
		self.numbercol = numbercol