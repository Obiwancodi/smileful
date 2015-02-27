from flask import render_template

from blog import app
from database import session
from models import Content
from models import User