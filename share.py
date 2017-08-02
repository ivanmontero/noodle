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

    def post(self):    
        logging.info("got some code")
        code = self.request.get("code")
        logging.info(code)
        if code:
            content_key = Code(content=code).put()
            logging.info(content_key)
            unique_id = content_key.id()
            logging.info(unique_id)
            logging.info("id = " + str(unique_id))
            self.response.write(unique_id)
            """
        template = jinja_environment.get_template('templates/share.html')
        self.response.out.write(template.render(unique_id=unique_id))
        """
    
class Code(ndb.Model):
    content = ndb.StringProperty()

class GetCode(webapp2.RequestHandler):
    def get(self):
        logging.info("retrieving now")
        id = int(self.request.get("key"))
        if id:
            logging.info("retrieving the key")
            file = Code.query().get_by_id(id)
            logging.info(file)

            if file:
                logging.info("id is valid")
        self.response.out.write(json.dumps(file=file))


        
   
