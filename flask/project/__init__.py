from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

def create_app():
	app = Flask(__name__)
	return app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres/my_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from .models import *

db.create_all()
db.session.commit()

@app.route('/')
def index():
	db.session.add(Numbercol(1))
	db.session.commit()
	return render_template('index.html')