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
            'title':        'Portland Review',
            'author':       {'nickname': 'C-Mo'},
            'body':         'Beautiful day in Portland!',
            'image_url':    'https://www.travelportland.com/wp-content/uploads/2013/04/portland-streetcar-downtown.jpg'
        },
        {
            'title':        'Avengers Movie Review',
            'author':       {'nickname': 'Rob'},
            'body':         'The Avengers movie was so cool!',
            'image_url':    'http://cdn.collider.com/wp-content/uploads/2017/02/the-avengers-group-image.jpg'
        }
    ]

    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
