from project import create_app
from flask import render_template

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')