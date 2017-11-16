#!flask/bin/python

# Import app variable from our app package
from app import app

# Invokes the run method to start the server
## Don't forget the app variable holds the Flask instance
app.run(debug=True)