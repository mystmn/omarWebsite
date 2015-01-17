"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app
from application import views

# My [Rules Start]
app.add_url_rule('/', 'home', view_func=views.home)

app.add_url_rule('/test', 'index', view_func=views.index)

app.add_url_rule('/beta', 'betaIndex', view_func=views.betaIndex)

app.add_url_rule('/beta/team', 'betaAbout', view_func=views.betaAbout)

app.add_url_rule('/alpha', 'alphaTest', view_func=views.alphaTest)

app.add_url_rule('/charley', 'charley', view_func=views.charley)

# [Rules End]

## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

