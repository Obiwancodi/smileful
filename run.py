import os
from flask.ext.script import Manager
from smileful import app
from getpass import getpass

from werkzeug.security import generate_password_hash
from smileful.models import User

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
    
from smileful.models import Content
from smileful.database import session

@manager.command
def seed():
    content = Content(link="https://www.youtube.com/watch?v=Q2daFOY9e4Q",
    genre="crass")
    session.add(content)
    session.commit()
    
    
@manager.command
def seed2():
    content = Content(link="http://www.biztechmagazine.com/article/2007/07/http-vs-https",
    genre="crass")
    session.add(content)
    session.commit()
    
@manager.command
def adduser():
    email = raw_input("Email: ")
    if session.query(User).filter_by(email=email).first():
        print "User with that email address already exists"
        return
     
    password = ""
    password_2 = ""
    while not (password and password_2) or password != password_2:
        password = getpass("Password: ")
        password_2 = getpass("Re-enter password: ")
    user = User(email=email,
                password=generate_password_hash(password))
    session.add(user)
    session.commit()

    


if __name__ == '__main__':
     manager.run()