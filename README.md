# Learning Python & Flask

This is my adventure of learning Python and Flask.

[![GitHub issues](https://img.shields.io/github/issues/infamousjoeg/learning-python-flask.svg?style=for-the-badge)](https://github.com/infamousjoeg/learning-python-flask/issues)[![GitHub stars](https://img.shields.io/github/stars/infamousjoeg/learning-python-flask.svg?style=for-the-badge)](https://github.com/infamousjoeg/learning-python-flask/stargazers)[![GitHub license](https://img.shields.io/github/license/infamousjoeg/learning-python-flask.svg?style=for-the-badge)](https://github.com/infamousjoeg/learning-python-flask/blob/master/LICENSE)

## Follow Along

I'm following the multi-part tutorial at [https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for this repo.

## Web Application

The tutorial walks you through developing a microblogging server that he calls _microblog_.

Here's some of the components he walks us through:

* User Management
* Database Management
* Web Forms
* Pagination of long lists
* Full text search
* Email notifications/alerts
* HTML Templates
  * I will be using [Editorial](https://html5up.net/uploads/images/editorial.jpg) from [HTML5 UP](https://html5up.net)
* Support for multiple languages
* Caching and performance optimizations
* Debugging techniques for dev/prod
  * I'm super excited about this one!
* Installation of all on prod server
  * I believe we end up using Heroku at the end of the tutorial

## Requirements

I tried this on Python 2.7, but found that Python 3 just worked.  eslint with cray-cray until I switched over the Py3... so just use it from the get-go and you'll be good.

Other than that, I used PowerShell in VS Code and went to town there for my terminal through out the tutorial.

## Install Python 3

Go here: [Download Python 3.x](https://www.python.org/downloads/)

## Install Flask

Create your `microblog` directory and then create a virtual environment for Python 3 for development by doing

```python
$ python -m venv flask
```

That will create a virtual environment for Python 3 in a directory named Flask.

## Flask Dependencies for Microblog

We'll use `pip` that was installed into our Python 3 virtual environment to download & install all necessary dependencies.

###### Linux/MacOS/Cygwin
```python
$ flask/bin/pip install flask
$ flask/bin/pip install flask-login
$ flask/bin/pip install flask-openid
$ flask/bin/pip install flask-mail
$ flask/bin/pip install flask-sqlalchemy
$ flask/bin/pip install sqlalchemy-migrate
$ flask/bin/pip install flask-whooshalchemy
$ flask/bin/pip install flask-wtf
$ flask/bin/pip install flask-babel
$ flask/bin/pip install guess_language
$ flask/bin/pip install flipflop
$ flask/bin/pip install coverage
```

###### Windows
```python
$ flask\Scripts\pip install flask
$ flask\Scripts\pip install flask-login
$ flask\Scripts\pip install flask-openid
$ flask\Scripts\pip install flask-mail
$ flask\Scripts\pip install flask-sqlalchemy
$ flask\Scripts\pip install sqlalchemy-migrate
$ flask\Scripts\pip install flask-whooshalchemy
$ flask\Scripts\pip install flask-wtf
$ flask\Scripts\pip install flask-babel
$ flask\Scripts\pip install guess_language
$ flask\Scripts\pip install flipflop
$ flask\Scripts\pip install coverage
```

## Start Tutorial

Now, you're ready to follow the wise words of Miguel Grinberg, [https://github.com/miguelgrinberg](https://github.com/miguelgrinberg)