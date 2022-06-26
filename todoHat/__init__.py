
from flask import Flask
# Configure application
app = Flask(__name__)
app.config["SECRET_KEY"] = 'ngf3u4gh9a87ghfvaewifj3fsdf'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

from todoHat import routs