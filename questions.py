# Core librarie
import webapp2
import os
import jinja2
import logging
# Parsing libraries
import json
import urllib2
# Authentification and database libraries
from google.appengine.api import users
from google.appengine.ext import ndb
# Get jinja environment from main
from main import jinja_environment

class User(ndb.Model):
    user_id = ndb.StringProperty()      # user.user_id()
    name = ndb.StringProperty()         # user.nickname()
    # question = ndb.StringProperty()

class Post(ndb.Model):  
    author = ndb.StringProperty()       # user.user_id()
    author_key = ndb.KeyProperty()      # (user model).key()
    question = ndb.StringProperty()     # the question
    content = ndb.StringProperty()      # text
    # media = ndb.BlobProperty()          # Images
    date = ndb.DateProperty()           # Date posted
    # votes = ndb.IntegerProperty()       
    post_type = ndb.StringProperty()    # either QUESTION or ANSWER
    # attached = ndb.KeyProperty(repeated=true)  # QUESTION: the answers
                                                 # ANSWER:   the question

class QuestionHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        data = { 
            "logged_in" : True if user else False,
            # Tests whether server is on Google's cloud or localhost
            "cloud_hosted" : os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')
        }
        if user:
            data["logout_url"] = users.create_logout_url('/questions')
            data["user_nickname"] = user.nickname()
            data["user_id"] = user.user_id()
        else:
            data["login_url"] = users.create_login_url('/questions')
        data["questions"] = [{'name': 'Jenessa', 'question': 'Does this work?'},
                        {'name': 'Ivan', 'question': 'Yes it does!'},
                        {'name': 'Ivan', 'question': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis pulvinar felis. Suspendisse potenti. Cras nibh urna, vehicula at commodo ac, imperdiet quis erat.'}]
        data["yourquestions"]=[{'name': 'Jenessa', 'question': 'Does this work?'},
                        {'name': 'Jenessa', 'question': 'Yes it does!'},]
        template = jinja_environment.get_template('templates/questions.html')
        self.response.out.write(template.render(data))


    
    def post(self):
        pass