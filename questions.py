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
                        {'name': 'Ivan', 'question': 'Vivamus pretium eu metus eget ornare. Quisque nec quam ipsum. Sed non dignissim nunc. Quisque eget dolor lorem?'},
                        {'name': 'Ivan', 'question': 'Nunc pharetra fringilla metus, in consequat leo dignissim at. Vestibulum porta suscipit dui, sit amet condimentum ex consectetur vel?'},
                        {'name': 'Ivan', 'question': 'Vestibulum in nunc ligula. Suspendisse tincidunt metus eget dui tincidunt ultricies. Etiam pellentesque porttitor dolor, cursus ultrices velit pulvinar vitae?'},
                        {'name': 'Ivan', 'question': 'Sed fringilla eget lorem sed euismod. Morbi pharetra molestie viverra. Nulla vel dapibus magna, et dignissim neque. Phasellus vel lacus sodales, tempor nulla vel, aliquam urna. Phasellus ac ipsum et velit rutrum imperdiet sit amet quis velit. Nam malesuada justo massa, in tincidunt enim lobortis in?'},
                        {'name': 'Ivan', 'question': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis pulvinar felis. Suspendisse potenti. Cras nibh urna, vehicula at commodo ac, imperdiet quis erat?'}]
        data["yourquestions"]=[{'name': 'Jenessa', 'question': 'Praesent velit neque, semper at nulla nec, elementum egestas dolor. Curabitur luctus magna mi, id efficitur nisl rhoncus eget?'},
                        {'name': 'Jenessa', 'question': 'Yes it does!'},
                        {'name': 'Jenessa', 'question': 'Aenean aliquet lectus eu sollicitudin facilisis. Integer purus lorem, sodales vitae egestas vel, auctor et lacus?'},
                        {'name': 'Jenessa', 'question': 'Etiam quam urna, fermentum in dictum ut, auctor eu ligula?'},
                        {'name': 'Jenessa', 'question': 'Nam at nulla non leo sagittis tempor. Phasellus orci risus, suscipit id vulputate eget, consectetur blandit velit?'}]
        template = jinja_environment.get_template('templates/questions.html')
        self.response.out.write(template.render(data))


    
    def post(self):
        pass