from flask import Flask, render_template

def create_app():
	app = Flask(__name__)
	app.config.from_object('config.ProdConfig')
	return app

app = create_app()

from .models import *

from .views import *