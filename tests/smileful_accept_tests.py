import os
import unittest
import multiprocessing
import time
from urlparse import urlparse

from werkzeug.security import generate_password_hash
from splinter import Browser


os.environ["CONFIG_PATH"] = "smileful.config.TestingConfig"

from smileful import app
from smileful import models
from smileful import login
from smileful.models import User, Scores, Content

from smileful.database import Base, engine, session



class TestViews(unittest.TestCase):
        
    def setUp(self):
        """ Test setup """
        
        self.browser = Browser("phantomjs")
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        # Set up the tables in the database
        Base.metadata.create_all(engine)

        # Create an example user
        self.user = models.User( email="alice@example.com",
                                password=generate_password_hash("test"))
        session.add(self.user)
        session.commit()

        self.process = multiprocessing.Process(target=app.run)
        self.process.start()
        time.sleep(5)
        
        
    def tearDown(self): 
    
        self.process.terminate()
        engine.dispose()
        session.close()
        Base.metadata.drop_all(engine)
        self.browser.quit()
        self.app_context.pop()
        
    def simulate_login(self):
        with self.client.session_transaction() as http_session:
            http_session["user_id"] = str(self.user.id)
            http_session["_fresh"] = True        
    
    def testLoginCorrect(self):
        
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")       
        
        
    
    def testLoginIncorrect(self):
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "bob@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/login")   
        
    def testNewLogin(self):
        self.browser.visit("http://0.0.0.0:5000/newlogin")
        self.browser.fill("email", "test5@test.com")
        self.browser.fill("password", "test5")
        self.browser.fill("password2", "test5")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        
    def testNewLoginwrongpass(self):
        self.browser.visit("http://0.0.0.0:5000/newlogin")
        self.browser.fill("email", "test5@test.com")
        self.browser.fill("password", "test5")
        self.browser.fill("password2", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/newlogin")

    def testNewLoginOldEmail(self):
        self.browser.visit("http://0.0.0.0:5000/newlogin")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test5")
        self.browser.fill("password2", "test5")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/newlogin")
        
    def testLogout(self):
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/logout")
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        
    def testPreferencesnotloggedin(self):
        self.browser.visit("http://0.0.0.0:5000/preferences")
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/login?next=%2Fpreferences")
     
    def testAddPreferences(self):
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/preferences")
        self.browser.choose('dark', '70')
        self.browser.choose('crass', '30')
        self.browser.choose('stand_up', '100')
        self.browser.choose('satire', '0')
        self.browser.choose('dry', '30')
        self.browser.choose('sketch_improv','100')
        self.browser.choose('slapstick', '30')
        self.browser.choose('pardoy', '70')
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        test_dict = {
            "dark": 70,
            "crass": 30,
            "stand_up": 100,
            "satire": 0,
            "dry": 30,
            "sketch_improv": 100,
            "slapstick": 30,
            "pardoy":70
        }
        
        user = session.query(User).filter(User.email == "alice@example.com").first()
        scores = session.query(Scores).filter(User.id == 1).first()
        
        self.assertEqual(scores.dark, 16)
        self.assertEqual(scores.crass, 6)
        self.assertEqual(scores.stand_up, 23)
        self.assertEqual(scores.satire, 0)
        self.assertEqual(scores.dry, 6)
        self.assertEqual(scores.sketch_improv, 23)
        self.assertEqual(scores.slapstick, 6)
        self.assertEqual(scores.pardoy, 16)

    def testAllPreferencesZero (self):
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/preferences")
        self.browser.choose('dark', '0')
        self.browser.choose('crass', '0')
        self.browser.choose('stand_up', '0')
        self.browser.choose('satire', '0')
        self.browser.choose('dry', '0')
        self.browser.choose('sketch_improv','0')
        self.browser.choose('topical','0')
        self.browser.choose('slapstick', '0')
        self.browser.choose('surreal', '0')
        self.browser.choose('pardoy', '0')
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/preferences")
        
        
    def testVulgarWant(self):
        
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/vulgar")
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        
        user = session.query(User).filter(User.email == "alice@example.com").first()
        
        self.assertEqual(user.want_vulgar,1)

    def testVulgarNot(self):
       
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/vulgar")
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/vulgar")
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        
        user = session.query(User).filter(User.email == "alice@example.com").first()
        
        self.assertEqual(user.want_vulgar,0)
  
    
    def testEditPreferences(self):
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/preferences")
        self.browser.choose('dark', '70')
        self.browser.choose('crass', '30')
        self.browser.choose('stand_up', '100')
        self.browser.choose('satire', '0')
        self.browser.choose('dry', '30')
        self.browser.choose('sketch_improv','100')
        self.browser.choose('slapstick', '30')
        self.browser.choose('pardoy', '70')
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        test_dict = {
            "dark": 70,
            "crass": 30,
            "stand_up": 100,
            "satire": 0,
            "dry": 30,
            "sketch_improv": 100,
            "slapstick": 30,
            "pardoy":70
        }
        
        
        self.browser.visit("http://0.0.0.0:5000/preferences")
        self.browser.choose('dark', '100')
        self.browser.choose('crass', '30')
        self.browser.choose('stand_up', '100')
        self.browser.choose('satire', '0')
        self.browser.choose('dry', '30')
        self.browser.choose('sketch_improv','0')
        self.browser.choose('slapstick', '30')
        self.browser.choose('pardoy', '70')
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        
        data ={
            "dark": 100,
            "crass": 30,
            "stand_up": 100,
            "satire": 0,
            "dry": 30,
            "sketch_improv": 0,
            "slapstick": 30,
            "pardoy":70
            }
        
        scores = session.query(Scores).filter(User.id == 1).first()  
        
        self.assertEqual(scores.dark, 27)
        self.assertEqual(scores.crass, 8)
        self.assertEqual(scores.stand_up, 27)
        self.assertEqual(scores.satire, 0)
        self.assertEqual(scores.dry, 8)
        self.assertEqual(scores.sketch_improv, 0)
        self.assertEqual(scores.slapstick, 8)
        self.assertEqual(scores.pardoy, 19)
        """
        Need to turn off methods=['POST'] for vulgar test to work on accpetance, but rewrite it back for intergration
    test to work. 
    """
    
    def testGetContentNoScores(self):
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/content")
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/content")
        
        user = session.query(User).filter(User.email == "alice@example.com").first()
        self.assertEqual(user.scores, None)
      
    def testGetContent(self):
        self.browser.visit("http://0.0.0.0:5000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/preferences")
        self.browser.choose('dark', '70')
        self.browser.choose('crass', '30')
        self.browser.choose('stand_up', '100')
        self.browser.choose('satire','30')
        self.browser.choose('dry', '30')
        self.browser.choose('sketch_improv','100')
        self.browser.choose('slapstick', '30')
        self.browser.choose('pardoy', '70')
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/home")
        self.browser.visit("http://0.0.0.0:5000/content")
        self.assertEqual(self.browser.url, "http://0.0.0.0:5000/content")
        
    """Try Button type submit for like/dislike/get_vulgar then go by number in listElement get(0) Should I test post for get_content?"""        
if __name__ == "__main__":
    unittest.main()        