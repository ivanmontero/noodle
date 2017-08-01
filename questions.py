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

import datetime

# TODO: Find a way to add time

class User(ndb.Model):
    user_id = ndb.StringProperty()      # user.user_id()
    nickname = ndb.StringProperty()         # user.nickname()
    questions = ndb.KeyProperty(repeated=True)
    answers = ndb.KeyProperty(repeated=True)
    # question = ndb.StringProperty()

class Question(ndb.Model):
    author_id = ndb.StringProperty()
    author_nickname = ndb.StringProperty()
    # author_key = ndb.KeyProperty()      # (user model).key()
    question = ndb.StringProperty()     # the question
    content = ndb.StringProperty()      # text
    # media = ndb.BlobProperty()          # Images
    # date = ndb.DateProperty()           # Date posted
    # votes = ndb.IntegerProperty()       
    answers = ndb.KeyProperty(repeated=True)

class Answer(ndb.Model):  
    author_id = ndb.StringProperty()
    author_nickname = ndb.StringProperty()
    # author_key = ndb.KeyProperty()      # (user model).key()
    content = ndb.StringProperty()      # text
    # media = ndb.BlobProperty()          # Images
    # date = ndb.DateProperty()           # Date posted
    # votes = ndb.IntegerProperty()       
    question = ndb.KeyProperty()

# Helper method to attach ID's with their questions
def formatRetrievableQuestions(questions):
    result=[]
    for i in questions:
        dres = i.to_dict()
        dres["id"] = i.key.id()
        result.append(dres)
    return result
    # for q in questions:
    #     q["id"] = q.key

class QuestionHandler(webapp2.RequestHandler):
    def get(self):
        # TO RETRIEVE QUESTION MODEL ASSOCIATED WITH QUESTION DIV:
        # logging.info(Question.get_by_id(5348024557502464).to_dict())
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
        # Test data
        data["questions"] = formatRetrievableQuestions(Question.query().fetch())
        # data["questions"] = [{'name': 'Jenessa', 'question': 'Does this work?'},
        #                 {'name': 'Ivan', 'question': 'Yes it does!'},
        #                 {'name': 'Ivan', 'question': 'Vivamus pretium eu metus eget ornare. Quisque nec quam ipsum. Sed non dignissim nunc. Quisque eget dolor lorem?'},
        #                 {'name': 'Ivan', 'question': 'Nunc pharetra fringilla metus, in consequat leo dignissim at. Vestibulum porta suscipit dui, sit amet condimentum ex consectetur vel?'},
        #                 {'name': 'Ivan', 'question': 'Vestibulum in nunc ligula. Suspendisse tincidunt metus eget dui tincidunt ultricies. Etiam pellentesque porttitor dolor, cursus ultrices velit pulvinar vitae?'},
        #                 {'name': 'Ivan', 'question': 'Sed fringilla eget lorem sed euismod. Morbi pharetra molestie viverra. Nulla vel dapibus magna, et dignissim neque. Phasellus vel lacus sodales, tempor nulla vel, aliquam urna. Phasellus ac ipsum et velit rutrum imperdiet sit amet quis velit. Nam malesuada justo massa, in tincidunt enim lobortis in?'},
        #                 {'name': 'Ivan', 'question': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis pulvinar felis. Suspendisse potenti. Cras nibh urna, vehicula at commodo ac, imperdiet quis erat?'}]
        data["yourquestions"]=[{'name': 'Jenessa', 'question': 'Praesent velit neque, semper at nulla nec, elementum egestas dolor. Curabitur luctus magna mi, id efficitur nisl rhoncus eget?'},
                        {'name': 'Jenessa', 'question': 'Yes it does!'},
                        {'name': 'Jenessa', 'question': 'Aenean aliquet lectus eu sollicitudin facilisis. Integer purus lorem, sodales vitae egestas vel, auctor et lacus?'},
                        {'name': 'Jenessa', 'question': 'Etiam quam urna, fermentum in dictum ut, auctor eu ligula?'},
                        {'name': 'Jenessa', 'question': 'Nam at nulla non leo sagittis tempor. Phasellus orci risus, suscipit id vulputate eget, consectetur blandit velit?'}]
        template = jinja_environment.get_template('templates/questions.html')
        self.response.out.write(template.render(data))
    

class NewQuestionHandler(webapp2.RequestHandler):
    def post(self):
        logging.info("Got a new question!")
        # Check if user is logged in
        user = users.get_current_user()
        if user:
            # Retrieve data
            question = self.request.get("question")
            content = self.request.get("content")
            # date = datetime.

            # Test if user object exists
            user_model = User.query(User.user_id == user.user_id()).get()
            if not user_model:
                # Create user object for new user
                user_model = User(user_id=user.user_id(), nickname=user.nickname())
                user_model.put()
                logging.info("New user created!")
            # Test for valid input
            if question and content:
                question_key = Question(author_id=user_model.user_id, author_nickname=user_model.nickname,
                    question=question, content=content).put()
                user_model.answers.append(question_key)
                logging.info("New question created!")
                user_model.put()

class GetQuestionsHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET questions recieved!")
        result = [i.to_dict() for i in Question.query().fetch()]
        # Remove all attached answer keys so an error isn't thrown
        for i in result:
            del i["answers"]
        self.response.write(json.dumps(result))

class GetQuestionHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET question recieved!")
        # Should recieve an ID of a question
        question_id = self.request.get("question_id")   #Might have to cast to int
        logging.info(question_id)
        # TODO: Get data from the question with the id passed and populate the
        # overlay template with the values in the question then return the html
        # in the response.
        question = Question.get_by_id(int(question_id))
        # self.response.write(question_id)
        if question:
            logging.info("question id is valid")
            data = question.to_dict()
            template = jinja_environment.get_template('templates/questions-overlay.html')
            self.response.out.write(template.render(data))

        

class NewAnswerHander(webapp2.RequestHandler):
    def post(self):
        logging.info("Got a new answer!")