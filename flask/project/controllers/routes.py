# -*- coding: utf-8 -*-

"""
This is where all the routes and controllers are defined.
"""

from flask import render_template, Blueprint

website_blueprint = Blueprint('website_blueprint', __name__)

@website_blueprint.route('/')
def index():
    # Controller logic should go here
	return render_template('index.html')
