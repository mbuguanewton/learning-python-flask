from flask import render_template
from app import app

# Create the mappings from URLs
@app.route('/')
@app.route('/index')

# Function to show index page
def index():
    user = {'nickname': 'Joe'} # fake user
    return render_template('index.html',
                            title='Home',
                            user=user)
