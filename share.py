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

        key = self.request.get("key")
        logging.info(key)
        if key:
            logging.info("Getting the code...")
            code = Code.get_by_id(int(key))
            dshared = code.to_dict()
            shared = dshared['content']
            logging.info(dshared['content'])
            # self.response.out.write(code.to_dict())
            """
            code_file = Code.get_by_id(code_id)
            if key:
                logging.info("code is valid!!!")
            """
        else:
            pass
        template = jinja_environment.get_template('templates/share.html')
        self.response.out.write(template.render(shared=shared))
        logging.info(shared)
        
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
            template = jinja_environment.get_template('templates/share.html')
            self.response.write(unique_id)
    
class Code(ndb.Model):
    content = ndb.StringProperty()


        
   
