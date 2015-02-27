from flask.ext.login import LoginManager

from blog import app
from database import session
from models import User

login_manager = LoginManager()
login_manager.init_app(app)