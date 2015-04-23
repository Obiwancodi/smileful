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
from smileful.models import User
from smileful.database import Base, engine, session



class TestViews(unittest.TestCase):
        
    def setUp(self):
        """ Test setup """
        
        self.browser = Browser("phantomjs")
    
        # Set up the tables in the database
        Base.metadata.create_all(engine)

        # Create an example user
        self.user = models.User( email="alice@example.com",
                                password=generate_password_hash("test"))
        session.add(self.user)
        session.commit()

        self.process = multiprocessing.Process(target=app.run)
        self.process.start()
        time.sleep(1)


    def tearDown(self):
        """ Test teardown """
        from multiprocessing.util import register_after_fork
        # Remove the tables and their data from the database
        register_after_fork(engine, engine.dispose)
        self.process.terminate()
        session.close()
        engine.dispose()
        Base.metadata.drop_all(engine)
        self.browser.quit()
        
        
    def testLoginCorrect(self):
        self.browser.visit("http://0.0.0.0:8080/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:8080/home")

    def testLoginIncorrect(self):
        self.browser.visit("http://0.0.0.0:8080/login")
        self.browser.fill("email", "bob@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:8080/login")   
        
    def testNewLogin(self):
        self.browser.visit("http://0.0.0.0:8080/newlogin")
        self.browser.fill("email", "test5@test.com")
        self.browser.fill("password", "test5")
        self.browser.fill("password2", "test5")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:8080/home")
        
    def testNewLoginwrongpass(self):
        self.browser.visit("http://0.0.0.0:8080/newlogin")
        self.browser.fill("email", "test5@test.com")
        self.browser.fill("password", "test5")
        self.browser.fill("password2", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://0.0.0.0:8080/newlogin")
        
if __name__ == "__main__":
    unittest.main()