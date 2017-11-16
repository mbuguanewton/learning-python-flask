from flask import render_template
from app import app

# Create the mappings from URLs
@app.route('/')
@app.route('/index')

# Function to show index page
def index():
    user = {'nickname': 'Joe'} # fake user
    posts = [ # fake array of posts
        {
            'author':   {'nickname': 'C-Mo'},
            'body':     'Beautiful day in Portland!'
        },
        {
            'author':   {'nickname': 'Rob'},
            'body':     'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
