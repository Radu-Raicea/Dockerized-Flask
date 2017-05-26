from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

def create_app():
	app = Flask(__name__)
	app.config.from_object('config.ProdConfig')
	return app

app = create_app()
db = SQLAlchemy(app)

from .models import *

db.create_all()
db.session.commit()

@app.route('/')
def index():
	db.session.add(Numbercol(1))
	db.session.commit()
	return render_template('index.html')