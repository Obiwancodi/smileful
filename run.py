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
    content = Content(link="http://en.wikipedia.org/wiki/Crass",
    genre="crass")
    session.add(content)
    session.commit()
    
    
@manager.command
def seed2():
    content = Content(link="http://bulbapedia.bulbagarden.net/wiki/Dark_%28type%29",
    genre="dark")
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

@manager.command
def seed3():
    content1 = Content(link="http://c2.com/cgi/wiki?DontRepeatYourself",
    genre="dry")
    content2 = Content(link="http://www.cc.com/stand-up",
                      genre="stand_up")
    content3 = Content(link="http://www.theonion.com/",
                      genre="satire")
    content4 = Content(link="http://goanimate.com/",
                      genre="animated")
    content5 = Content(link="http://alwaysfunny.com/",
                      genre="topical")
    content6 = Content(link="http://dictionary.reference.com/browse/slapstick",
                      genre="slapstick")
    content7 = Content(link="http://en.wikipedia.org/wiki/Surreal",
                      genre="surreal")
    content8 = Content(link="http://en.wikipedia.org/wiki/Situational_leadership_theory",
                      genre="situational")
    content9 = Content(link="http://improv.com/index.cfm",
                      genre="improv")
    session.add_all([content1,content2,content3,content4,content5,content6,content7,content8,content9])
    session.commit()


if __name__ == '__main__':
     manager.run()