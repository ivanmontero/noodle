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
# Core library
import webapp2
import jinja2
import os

# global jinja_environment
global jinja_environment
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# ====================== IMPORT HANDLER FILES HERE ======================
from template import *
from index import *
# ====================== IMPORT HANDLER FILES HERE ======================

# ========================== ADD HANDLERS HERE ==========================
app = webapp2.WSGIApplication([
    ('/', PleasePutYourHandlerNameHere)
], debug=True)
# ========================== ADD HANDLERS HERE ==========================
