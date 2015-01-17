"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
from forms import ExampleForm
from models import ExampleModel


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def home():
    return render_template('home.html')

def index():
    user = {'name': 'Paul'}
    title = "Paul Cameron"
    return render_template('topHeader.html', user=user, title=title)

def betaIndex():
    title = "Index"
    return render_template('/beta/index.html', title=title)

def betaAbout():
    title = "About"
    return render_template('/beta/team.html', title=title)

def alphaTest():
    title = "Testing Env"
    return render_template('/alpha/home.html', title=title)

def charley():
    title = "Testing Env"
    return render_template('charleyTest.html', title=title)

def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

