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

# Google+ API Key (for getting user image): AIzaSyBTXhazY7-0epr_F1ardo8CHOA9afRXfuc

class IndexHandler(webapp2.RequestHandler):
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
            # Testing purposes, My ID: 114783711473680853748
            if(data["cloud_hosted"]):
                data["user_image"] = json.loads(urllib2.urlopen("https://www.googleapis.com/plus/v1/people/" 
                    + str(user.user_id()) + "?fields=image&key=AIzaSyBTXhazY7-0epr_F1ardo8CHOA9afRXfuc").read())["image"]["url"]
            else:
                data["user_image"] = "/res/img/anon-pic.png"
        else:
            data["login_url"] = users.create_login_url('/')
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(data))
    
    def post(self):
        pass