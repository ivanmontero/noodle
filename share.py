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

class ShareHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        data = { 
            "logged_in" : True if user else False,
            # Tests whether server is on Google's cloud or localhost
            "cloud_hosted" : os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')
        }
        if user:
            data["logout_url"] = users.create_logout_url('/share')
            data["user_nickname"] = user.nickname()
            data["user_id"] = user.user_id()
        else:
            data["login_url"] = users.create_login_url('/share')
        template = jinja_environment.get_template('templates/share.html')
        self.response.out.write(template.render(data))
    
class Code(ndb.Model):
    content = ndb.StringProperty()

class GetQuestion(webapp2.RequestHandler):
    def get(self):
        logging.info("retrieving the key")
        code_id = self.request.get("code_id")
        logging.info(code_id)
        
        code = Code.get_by_id(int(code_id))

        if code_id:
            logging.info("id is valid")

        template = jinja_environment.get_template('templates/share.html')
        self.response.out.write(template.render(id=result))

    def post(self):
        logging.info("got some code")
        code = self.request.get("code")
        if code:
            content_key = Code(content=code).put()
            unique_id = content_key.id()
            logging.info("id = " + unique_id)
