import os
import unittest
import webtest
from urlparse import urlparse

from werkzeug.security import generate_password_hash
from flask.ext.webtest import TestApp

# Configure your app to use the testing database
os.environ["CONFIG_PATH"] = "smileful.config.TestingConfig"


from smileful import app
from smileful import models
from smileful import login
from smileful.views import calculate_score, get_content, preferences_post
from smileful.models import User, Scores, Content
from smileful.database import Base, engine, session
from werkzeug.security import check_password_hash


class TestViews(unittest.TestCase):
    def setUp(self):
        """ Test setup """
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
        
        
        # Set up the tables in the database
        Base.metadata.create_all(engine)

        

        # Create an example user
        self.user = models.User(email="alice@example.com",
                                password=generate_password_hash("test"))
        self.user1 = models.User(email="yes@example.com",
                               password=generate_password_hash("test2"))
        
        
        self.content1 = models.Content(link="https://www.youtube.com/watch?v=9FPv2toi5og", genre="stand_up", vulgar=1)
        self.content2 = models.Content(link="https://www.youtube.com/watch?v=HjLr7Duq3B8", genre="stand_up")
        self.content3 = models.Content(link="https://www.youtube.com/watch?v=3qqE_WmagjY", genre="sketch_improv", vulgar=1)
        self.content4 = models.Content(link="https://www.youtube.com/watch?v=kMwiBBCLT3o", genre="sketch_improv")
        self.content5 = models.Content(link="http://www.cc.com/video-clips/tp6kjq/comedy-central-presents-don-t-stab-me", genre="dark")
        self.content6 = models.Content(link="http://www.cc.com/video-clips/9y43ia/comedy-central-presents-too-graphic--too-sad", genre="dark")
        self.content7 = models.Content(link="https://www.youtube.com/watch?v=oPpzJAzdpTU", genre="pardoy")
        self.content8 = models.Content(link="https://www.youtube.com/watch?v=Ol2DedEhOGI", genre="pardoy", vulgar=1)
        self.content9 = models.Content(link="https://www.youtube.com/watch?v=2AAa0gd7ClM", genre="satire")
        self.content10 = models.Content(link="https://www.youtube.com/watch?v=Zugm5fGtNiA", genre="satire")
        self.content11 = models.Content(link="https://www.youtube.com/watch?v=WxuhISNpZFk", genre="dry", vulgar=1)
        self.content12 = models.Content(link="http://www.cc.com/video-clips/fb5nqp/comedy-central-presents-southern-accents", genre="dry")
        self.content13 = models.Content(link="https://www.youtube.com/watch?v=fUEd2dyItuE", genre="topical", vulgar=1)
        self.content14 = models.Content(link="https://www.youtube.com/watch?v=oMCKaBku83U", genre="topical")
        self.content15 = models.Content(link="https://www.youtube.com/watch?v=FIGL4eaks20", genre="slapstick", vulgar=1)
        self.content16 = models.Content(link="https://www.youtube.com/watch?v=jhaqJXHIXiA", genre="slapstick")
        self.content17 = models.Content(link="http://www.bing.com/videos/search?q=crass%20comedy&qs=n&form=QBVR&pq=crass%20comedy&sc=6-12&sp=-1&sk=#view=detail&mid=D915FA68B2A400920E30D915FA68B2A400920E30", genre="crass")
        self.content18 = models.Content(link="http://www.bing.com/videos/search?q=crass%20comedy&qs=n&form=QBVR&pq=crass%20comedy&sc=6-12&sp=-1&sk=#view=detail&mid=6A5CB6E166D57FCDD5836A5CB6E166D57FCDD583", genre="crass", vulgar = 1)
        self.content19 = models.Content(link="http://www.bing.com/videos/search?q=surreal%20comedians&qs=n&form=QBVR&pq=surreal%20comedians&sc=2-17&sp=-1&sk=#view=detail&mid=8E38C278DEA4752CC1E38E38C278DEA4752CC1E3", genre="surreal")
        self.content20 = models.Content(link="http://www.cc.com/video-clips/9gz49q/premium-blend-brutally-honest", genre="surreal")
        
        
        session.add_all([self.user,self.user1,self.content1,self.content2,self.content3,self.content4,self.content5,self.content6,self.content7,self.content8,self.content9,self.content10,self.content11,self.content12,self.content13,self.content14,self.content15,self.content16,self.content17,self.content18,self.content19,self.content20])
        session.commit()
        
        

    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)
        self.app_context.pop()
        
        
    def simulate_login(self):
        with self.client.session_transaction() as http_session:
            http_session["user_id"] = str(self.user.id)
            http_session["_fresh"] = True
        
        
    def testcalculatescore (self):
        
        user = session.query(User).filter(User.email =="alice@example.com").first()
        scores = Scores(user_id = user.id)
        
        test_dict = {
            "dark": 70,
            "crass": 30,
            "stand_up": 100,
            "satire": 0,
            "dry": 30,
            "sketch_improv": 100,
            "topical": 0,
            "slapstick": 30,
            "surreal": 0,
            "pardoy":70
        }
        
        calculate_score(scores,test_dict)
        
        self.assertEqual(scores.dark, 16)
        self.assertEqual(scores.crass, 6)
        self.assertEqual(scores.stand_up, 23)
        self.assertEqual(scores.satire, 0)
        self.assertEqual(scores.dry, 6)
        self.assertEqual(scores.sketch_improv, 23)
        self.assertEqual(scores.topical, 0)
        self.assertEqual(scores.slapstick, 6)
        self.assertEqual(scores.surreal, 0)
        self.assertEqual(scores.pardoy, 16)
        
    def testcalculatescorezero(self):
        user = session.query(User).filter(User.email =="alice@example.com").first()
        scores = Scores(user_id = user.id)
        
        test_dict = {
            "dark": 0,
            "crass": 0,
            "stand_up": 0,
            "satire": 0,
            "dry": 0,
            "sketch_improv": 0,
            "topical": 0,
            "slapstick": 0,
            "surreal": 0,
            "pardoy":0
        }
        
        self.assertEqual(scores.dark, None)
        self.assertEqual(scores.crass, None)
        self.assertEqual(scores.stand_up, None)
        self.assertEqual(scores.satire, None)
        self.assertEqual(scores.dry, None)
        self.assertEqual(scores.sketch_improv, None)
        self.assertEqual(scores.topical, None)
        self.assertEqual(scores.slapstick, None)
        self.assertEqual(scores.surreal, None)
        self.assertEqual(scores.pardoy, None)
        
        
    def testgetcontent (self):
        self.simulate_login()
        user = self.user
        scores = Scores(user_id = user.id)
        
        content1 = session.query(Content).filter(Content.id == 20).first()
        content2 = session.query(Content).filter(Content.id == 17).first()
        content3 = session.query(Content).filter(Content.id == 15).first()
        content4 = session.query(Content).filter(Content.id == 6).first()
        
        scores.dark = 16
        scores.crass = 6
        scores.stand_up = 23
        scores.satire = 0
        scores.dry = 6
        scores.stetch_improv = 23
        scores.topical = 0 
        scores.slapstick = 6
        scores.surreal = 0
        scores.pardoty = 16
        
        
        user.want_vulgar = 1
        
        user.dislike_content = [content1, content2]
        
        user.seen_content = [content3, content4]
        
        response = self.client.get("/content", data={
                "content":"content"
            })
        
        
        
        self.assertEqual(response.status_code,200)
        self.assertNotEqual(content.id, 20)
        
    def testlike(self):
        self.simulate_login()
        user = self.user
        scores = Scores(user_id = user.id)
        
        content1 = session.query(Content).filter(Content.id == 20).first()
        content2 = session.query(Content).filter(Content.id == 17).first()
        content3 = session.query(Content).filter(Content.id == 15).first()
        content4 = session.query(Content).filter(Content.id == 6).first()
        
        scores.dark = 16
        scores.crass = 6
        scores.stand_up = 23
        scores.satire = 0
        scores.dry = 6
        scores.stetch_improv = 23
        scores.topical = 0 
        scores.slapstick = 6
        scores.surreal = 0
        scores.pardoty = 16
        
        response = self.client.post("/content", data = {
                "like_dislike_vulgar":"like",
                "content":"content1"
                
            })
        self.assertEqual(response.status_code,302)
        
    def testAddPreferences(self):
        """It makes the correct dict of scores and adds them to dict in the view function but for some reason won't add to scores in the test funciton.  Is there a way to make sure the dicts are both the same (one from the function and one from the test?) Also how to I test that it creates a score realtionship with user?"""
        self.simulate_login()
        user = self.user
        scores = Scores(user_id = user.id)
        
        response = self.client.post("/preferences", data ={
            "dark": 70,
            "crass": 30,
            "stand_up": 100,
            "satire": 0,
            "dry": 30,
            "sketch_improv": 100,
            "topical": 0,
            "slapstick": 30,
            "surreal": 0,
            "pardoy":70
            })
        
        test_dict = {
            "dark": 70,
            "crass": 30,
            "stand_up": 100,
            "satire": 0,
            "dry": 30,
            "sketch_improv": 100,
            "topical": 0,
            "slapstick": 30,
            "surreal": 0,
            "pardoy":70
        }
        
        calculate_score(scores,test_dict)
        
        self.assertEqual(response.status_code,302)
        self.assertEqual(urlparse(response.location).path, "/home")
        self.assertEqual(scores.dark, 16)
        self.assertEqual(scores.crass, 6)
        self.assertEqual(scores.stand_up, 23)
        self.assertEqual(scores.satire, 0)
        self.assertEqual(scores.dry, 6)
        self.assertEqual(scores.sketch_improv, 23)
        self.assertEqual(scores.topical, 0)
        self.assertEqual(scores.slapstick, 6)
        self.assertEqual(scores.surreal, 0)
        self.assertEqual(scores.pardoy, 16)

    def testLogin(self):
        
        user = session.query(User).filter_by(email="alice@example.com").first()
        content2 = session.query(Content).filter(Content.id == 17).first()
        content3 = session.query(Content).filter(Content.id == 18).first()
        
        
        
        user.user_seen_content = [content2,content3]
        
        response = self.client.post("/login", data = {
                "email":"alice@example.com",
                "password": "test"
            })
        
        self.assertEqual(response.status_code,302)
        self.assertEqual(user.user_seen_content,[])
        self.assertEqual(urlparse(response.location).path, "/home")
        
        
    def testwrongLoginPasswordFlash(self):
        user = session.query(User).filter_by(email="alice@example.com").first()
        
        response = self.client.post("/login", follow_redirects=True, data = {
                "email":"alice@example.com",
                "password": "test1"
            })
        
        
        self.assertEqual(response.status_code, 200)
        
        assert 'Incorrect username or password' in response.data
        
    def testWrongLoginPassword(self):       
        user = session.query(User).filter_by(email="alice@example.com").first()
        
        response = self.client.post("/login", data = {
                "email":"alice@example.com",
                "password": "test1"
            })
        
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, "/login")
              
    
    def testwrongLoginEmail(self):
        "Ask if 302 is the correct response I should be getting"
        user = session.query(User).filter_by(email="alice@example.com").first()
        
        response = self.client.post("/login", data = {
                "email":"alice1@example.com",
                "password": "test"
            })
        
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, "/login")
        
    def testWrongLoginEmailFlash(self):
        user = session.query(User).filter_by(email="alice@example.com").first()
        
        response = self.client.post("/login", follow_redirects=True, data = {
                "email":"alice1@example.com",
                "password": "test"
            })
        
        
        self.assertEqual(response.status_code, 200)
        
        assert 'Incorrect username or password' in response.data
        
        
    def testwrongLogin(self):
        user = session.query(User).filter_by(email="alice@example.com").first()
        
        response = self.client.post("/login", data = {
                "email":"alice1@example.com",
                "password": "test1"
            })
        
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, "/login")
        
        
    def testWrongLoginFlash(self):
        
        user = session.query(User).filter_by(email="alice@example.com").first()
        
        response = self.client.post("/login",follow_redirects=True, data = {
                "email":"alice1@example.com",
                "password": "test1"
            })
        
        
        self.assertEqual(response.status_code, 200)
        
        assert 'Incorrect username or password' in response.data
        
    def testnewLogin(self):

        response = self.client.post("/newlogin", data = {
                "email": "test7@test.com",
                "password": "test7",
                "password2": "test7"
            })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, "/home")
        
        users = session.query(models.User).all()
        self.assertEqual(len(users), 3)
        
        user = users[2]
        
        password = "test7"
        
        self.assertEqual(user.email, "test7@test.com")
        self.assertEqual(True,check_password_hash(user.password,password))
        
        
    def testWrongPassword2(self):
        
        response = self.client.post("/newlogin", data = {
                "email": "test7@test.com",
                "password": "test7",
                "password2": "test6"
            })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, "/newlogin")
        
        
    def testwrongPassword2Flash (self):
        
        response = self.client.post("/newlogin",follow_redirects=True, data = {
                "email": "test7@test.com",
                "password": "test7",
                "password2": "test6"
            })
        
        self.assertEqual(response.status_code, 200)
        
        assert 'Passwords do not match' in response.data

    def testEmailAlreadyExist(self):
        
        response = self.client.post("/newlogin", data = {
                "email":"alice@example.com",
                "password": "test1",
                "password2": "test1"
            })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, "/newlogin")

    def testEmailAlreadyExistFlash(self):
        
        response = self.client.post("/newlogin",follow_redirects=True, data = {
                "email": "alice@example.com",
                "password": "test1",
                "password2": "test2"
            })
        
        self.assertEqual(response.status_code, 200)
        
        assert 'Email already used by another account' in response.data
        
    def testvulgarno(self):
        
        self.simulate_login()
        user = self.user
        user.want_vulgar = 0
        print user.want_vulgar
        
        response = self.client.post("/vulgar", data = {
                "user.want_vulgar": "0"
            })
        
        self.assertEqual(response.status_code,302)
        self.assertEqual(user.want_vulgar,1)
        
        
    def testvulgarnoFlash(self):
        
        self.simulate_login()
        user = self.user
        user.want_vulgar = 0
        print user.want_vulgar
        
        response = self.client.post("/vulgar", follow_redirects=True, data = {
                "user.want_vulgar": "0"
            })
        
        self.assertEqual(response.status_code,200)
        assert 'Vulgar Content Turned Off' in response.data
        
    def testvulgaryes(self):
        
        self.simulate_login()
        user = self.user
        user.want_vulgar = 1
        
        response = self.client.post("/vulgar", data = {
                "user.want_vulgar": "1"
            })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.want_vulgar, 0)

    def testvulgaryesFlash(self):
        
        self.simulate_login()
        user = self.user
        user.want_vulgar = 1
        print user.want_vulgar
        
        response = self.client.post("/vulgar", follow_redirects=True, data = {
                "user.want_vulgar": "1"
            })
        
        self.assertEqual(response.status_code,200)
        assert 'Vulgar Content Turned On' in response.data
        
        
if __name__ == "__main__":
    unittest.main()       