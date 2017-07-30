# Core libraries
import webapp2
import os
import jinja2
import logging
# Parsing libraries
import json
import urllib2
# Authentification and databasse libraries
from google.appengine.api import users
from google.appengine.ext import ndb
# Get jinja environment from main
from main import jinja_environment

class PleasePutYourHandlerNameHere(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/your_template_name_here.html')
        self.response.out.write(template.render())
    
    def post(self):
        pass