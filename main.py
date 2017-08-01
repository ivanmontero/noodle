# SCRATCH ALL IDEAS

# Suggestions:
# - Use Bootstrap for CSS

# Core library
import webapp2
import jinja2
import os

# global jinja_environment
global jinja_environment
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

# ====================== IMPORT HANDLER FILES HERE ======================
from index import *
from questions import *
from share import *
from editor import *
from wiki import *
# ====================== IMPORT HANDLER FILES HERE ======================


# ========================== ADD HANDLERS HERE ==========================
app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/questions', QuestionHandler),
    ('/questions/newquestion', NewQuestionHandler),
    ('/questions/getquestions', GetQuestionsHandler),
    ('/questions/getquestion', GetQuestionHandler),
    ('/share', ShareHandler),
    ('/editor', EditorHandler),
    ('/wiki', WikiHandler)
], debug=True)
# ========================== ADD HANDLERS HERE ==========================
