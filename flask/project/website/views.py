# -----------------------------------------------
# This is where all the routes are defined.
# -----------------------------------------------


from flask import render_template, Blueprint


website_blueprint = Blueprint('website_blueprint', __name__)


# Endpoints are defined defined by applying a decorator on a function.
# The '/' route points to the root of the website.
# The return value of this function specifies what is returned when
# an HTTP request is made at this endpoint. In this case, Flask renders
# the template called 'index.html', which is located in the following
# location by default: flask/project/templates/
@website_blueprint.route('/')
def index():
	return render_template('index.html')
