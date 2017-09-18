# ------------------------------------------------------------------
# This is the root of the main package of the Flask app: project.
#
# Whenever you see 'from project import [something]', it takes it
# from here.
# ------------------------------------------------------------------


from flask import Flask, g, request, current_app
from flask_sqlalchemy import SQLAlchemy
import os
import logging


# Defines the format of the logging to include the time and to use the INFO logging level or worse.
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)


db = SQLAlchemy()


# Defines the application factory. Every time this function is called, a new application
# instance is created. The reason why an application factory is needed is because we
# need to use different configurations for running our tests.
def create_app():
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    # Imports the 'website_blueprint' to apply it to the application instance.
    # In order to define routes/endpoints in Flask, you need to write something
    # like @app.route('/endpoint1'). Since we don't initialize our application
    # variable here, but use an application factory instead, we can't import 'app'.
    #
    # Instead, blueprints are used. If you want to read more about it, visit:
    # http://flask.pocoo.org/docs/0.12/blueprints/
    from project.website.views import website_blueprint
    app.register_blueprint(website_blueprint)

    return app
