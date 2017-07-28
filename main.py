# TODO:
# - Split each website into it's own .py file

# Features:
# - About us
# - Calendar
# - Search (General, Photos, etc)
# - Games
# - Photos
# - Checkers
# - Social Media
# - Blog ("The Noodle")
# - Noodle News

# Suggestions:
# - Use Bootstrap for CSS

# ========================= LIBRARIES =========================
# Core libraries
import webapp2
import os
import sys
import jinja2
import logging
# Parsing libraries
import json
import urllib2
# Authentification and databasse libraries
from google.appengine.api import users
from google.appengine.ext import ndb
# To allow Python to import from handlers/ folder
# sys.path.append('/handlers')
# Other pages
# from handlers.index import *
# TODO

# jinja initialization
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')
        # template = jinja_environment.get_template('templates/index.html')
        # self.response.out.write(template.render())
        # test_function()





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
