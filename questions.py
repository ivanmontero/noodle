# Core librarie
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

class User(ndb.Model):
    name = ndb.StringProperty()
    question = ndb.StringProperty()

class Post(ndb.Model):
    author = ndb.StringProperty()
    content = ndb.StringProperty()
    media = ndb.BlobProperty()
    date = ndb.DateProperty()
    votes = ndb.IntegerProperty()
    post_type = ndb.StringProperty()
    
class QuestionHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        data = { 
            "logged_in" : True if user else False,
            # Tests whether server is on Google's cloud or localhost
            "cloud_hosted" : os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')
        }
        if user:
            data["logout_url"] = users.create_logout_url('/')
            data["user_nickname"] = user.nickname()
            data["user_id"] = user.user_id()
        else:
            data["login_url"] = users.create_login_url('/')
        template = jinja_environment.get_template('templates/questions.html')
        self.response.out.write(template.render(data))


    
    def post(self):
        pass