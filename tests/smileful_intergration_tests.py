import os
import unittest
from urlparse import urlparse

from werkzeug.security import generate_password_hash


# Configure your app to use the testing database
os.environ["CONFIG_PATH"] = "smileful.config.TestingConfig"


from smileful import app
from smileful import models
from smileful import login
from smileful.views import calculate_score, get_content, preferences_post, add_scores
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
        
        
        session.add_all([self.user,self.content1,self.content2,self.content3,self.content4,self.content5,self.content6,self.content7,self.content8,self.content9,self.content10,self.content11,self.content12,self.content13,self.content14,self.content15,self.content16,self.content17,self.content18,self.content19,self.content20])
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
        
        score_dict = {
            "dark": 16,
            "crass": 6,
            "stand_up": 23,
            "satire": 0,
            "dry": 6,
            "sketch_improv": 23,
            "slapstick": 6,
            "pardoy": 16
            
        }
        
        compare_dict = calculate_score(test_dict)
        
        self.assertEqual(compare_dict, score_dict)
        
        
    def testAddScores(self):
        
        user = session.query(User).filter(User.email =="alice@example.com").first()
        scores = Scores(user_id = user.id)
        
        
        
        score_dict = {
            "dark": 16,
            "crass": 6,
            "stand_up": 23,
            "satire": 0,
            "dry": 6,
            "sketch_improv": 23,
            "slapstick": 6,
            "pardoy": 16
            
        }
        
        
        add_scores(scores, score_dict)
    
        self.assertEqual(scores.dark, 16)
        self.assertEqual(scores.crass, 6)
        self.assertEqual(scores.stand_up, 23)
        self.assertEqual(scores.satire, 0)
        self.assertEqual(scores.dry, 6)
        self.assertEqual(scores.sketch_improv, 23)
        self.assertEqual(scores.slapstick, 6)
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
            "slapstick": 0,
            "pardoy":0
        }
        
        self.assertEqual(scores.dark, None)
        self.assertEqual(scores.crass, None)
        self.assertEqual(scores.stand_up, None)
        self.assertEqual(scores.satire, None)
        self.assertEqual(scores.dry, None)
        self.assertEqual(scores.sketch_improv, None)
        self.assertEqual(scores.slapstick, None)
        self.assertEqual(scores.pardoy, None)
        
    

    def testAddPreferences(self):
        
        self.simulate_login()
        
        response = self.client.post("/preferences", data ={
            "dark": 70,
            "crass": 30,
            "stand_up": 100,
            "satire": 0,
            "dry": 30,
            "sketch_improv": 100,
            "slapstick": 30,
            "pardoy":70
            })
        
        
        
        
        scores = session.query(Scores).filter(User.id == 1).first()
        
        
        
        self.assertEqual(response.status_code,302)
        self.assertEqual(urlparse(response.location).path, "/home")
        self.assertEqual(scores.dark, 16)
        self.assertEqual(scores.crass, 6)
        self.assertEqual(scores.stand_up, 23)
        self.assertEqual(scores.satire, 0)
        self.assertEqual(scores.dry, 6)
        self.assertEqual(scores.sketch_improv, 23)
        self.assertEqual(scores.slapstick, 6)
        self.assertEqual(scores.pardoy, 16)
    
    
    def testAddPreferencesAllZero(self):
        
        self.simulate_login()
        
        response = self.client.post("/preferences", data ={
            "dark": 0,
            "crass": 0,
            "stand_up": 0,
            "satire": 0,
            "dry": 0,
            "sketch_improv": 0,
            "slapstick": 0,
            "pardoy": 0
            })
        
        scores = session.query(Scores).filter(User.id == 1).first()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(scores, None)

    def testAddPreferencesEdit(self):
        
        self.simulate_login()
        
        user = session.query(User).filter(User.email =="alice@example.com").first()
        scores = Scores(user_id = user.id)
        
        scores.dark = 16
        scores.crass = 15
        scores.stand_up = 4
        scores.satire = 15
        scores.dry = 12
        scores.sketch_imporv = 0
        scores.slapstick = 9
        scores.pardoy = 12
        
        
        
        response = self.client.post("/preferences", data ={
            "dark": 100,
            "crass": 30,
            "stand_up": 100,
            "satire": 0,
            "dry": 30,
            "sketch_improv": 0,
            "slapstick": 30,
            "pardoy":70
            })
        
        
        
        
        scores = session.query(Scores).filter(User.id == 1).first()
        
        
        
        self.assertEqual(response.status_code,302)
        self.assertEqual(urlparse(response.location).path, "/home")
        self.assertEqual(scores.dark, 27)
        self.assertEqual(scores.crass, 8)
        self.assertEqual(scores.stand_up, 27)
        self.assertEqual(scores.satire, 0)
        self.assertEqual(scores.dry, 8)
        self.assertEqual(scores.sketch_improv, 0)
        self.assertEqual(scores.slapstick, 8)
        self.assertEqual(scores.pardoy, 19)

    
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
        self.assertEqual(len(users), 2)
        
        user = users[1]
        
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
        user = session.query(User).filter(User.email == "alice@example.com").first()
        user.want_vulgar = 0
        print user.want_vulgar
        
        response = self.client.post("/vulgar", data = {
                "user.want_vulgar": "0"
            })
        user = session.query(User).filter(User.email == "alice@example.com").first()
        self.assertEqual(response.status_code,302)
        self.assertEqual(user.want_vulgar,1)
        
        
    def testvulgarnoFlash(self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        user.want_vulgar = 0
       
        
        response = self.client.post("/vulgar", follow_redirects=True, data = {
                "user.want_vulgar": "0"
            })
        user = session.query(User).filter(User.email == "alice@example.com").first()
        self.assertEqual(response.status_code,200)
        assert 'Vulgar Content Turned Off' in response.data
        
    def testvulgaryes(self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        user.want_vulgar = 1
        
        response = self.client.post("/vulgar", data = {
                "user.want_vulgar": "1"
            })
        user = session.query(User).filter(User.email == "alice@example.com").first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.want_vulgar, 0)

    def testvulgaryesFlash(self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        user.want_vulgar = 1
        
        
        response = self.client.post("/vulgar", follow_redirects=True, data = {
                "user.want_vulgar": "1"
            })
        
        user = session.query(User).filter(User.email == "alice@example.com").first()
        self.assertEqual(response.status_code,200)
        assert 'Vulgar Content Turned On' in response.data
        
        
    def testGetContentDisliked(self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        scores = Scores(user_id = user.id)
        session.add(scores)
        
        scores.dark = 0
        scores.crass = 0
        scores.stand_up = 100
        scores.satire = 0
        scores.dry = 0
        scores.sketch_imporv = 0
        scores.slapstick = 0
        scores.pardoy = 0
        
        
        content1 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=9FPv2toi5og").first()
        content2 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=HjLr7Duq3B8").first()
        
        user.dislike_content = [content1]
        disliked_content = [content.id for content in user.dislike_content]
        print"This is user disliked content"
        print disliked_content
        
        response = self.client.get("/content")
        user = session.query(User).filter(User.email == "alice@example.com").first()
        print "This is user seen content"
        seen = [content.id for content in user.user_seen_content]
        print seen
        self.assertEqual(response.status_code, 200)
        self.assertEqual(seen, [2])

    def testGetContentSeen (self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        scores = Scores(user_id = user.id)
        session.add(scores)
        
        scores.dark = 0
        scores.crass = 0
        scores.stand_up = 100
        scores.satire = 0
        scores.dry = 0
        scores.sketch_imporv = 0
        scores.slapstick = 0
        scores.pardoy = 0
        
        content1 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=9FPv2toi5og").first()
        content2 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=HjLr7Duq3B8").first()
        
        
        user.user_seen_content = [content1]
        seen = [content.id for content in user.user_seen_content]
        self.assertEqual(seen, [1])
        
        response = self.client.get("/content")
        user = session.query(User).filter(User.email == "alice@example.com").first()
        seen = [content.id for content in user.user_seen_content]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(seen, [1,2])
        
        
    def testGetContentNotVulgar(self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        user.want_vulgar = 1
        scores = Scores(user_id = user.id)
        session.add(scores)
        
        scores.dark = 0
        scores.crass = 0
        scores.stand_up = 100
        scores.satire = 0
        scores.dry = 0
        scores.sketch_imporv = 0
        scores.slapstick = 0
        scores.pardoy = 0
        
        content1 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=9FPv2toi5og").first()
        content2 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=HjLr7Duq3B8").first()
        
        print "this is content 2 id"
        print content2.id
        
        response = self.client.get("/content")
        
        user = session.query(User).filter(User.email == "alice@example.com").first()
        seen = [content.id for content in user.user_seen_content]
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(seen, [2])
        
    def testGetContentNoContentLeft(self):
    
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        scores = Scores(user_id = user.id)
        session.add(scores)
        
        scores.dark = 0
        scores.crass = 0
        scores.stand_up = 100
        scores.satire = 0
        scores.dry = 0
        scores.sketch_imporv = 0
        scores.slapstick = 0
        scores.pardoy = 0
        
        content1 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=9FPv2toi5og").first()
        content2 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=HjLr7Duq3B8").first()
        content3 = session.query(Content).filter(Content.link == "https://www.youtube.com/watch?v=kMwiBBCLT3o").first()
        
        user.user_seen_content = [content1,content2]
        seen = [content.id for content in user.user_seen_content]
        
        response = self.client.get("/content")
        
        user = session.query(User).filter(User.email == "alice@example.com").first()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(seen, [1,2])
        
      
    def testContentDislikeContent(self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        scores = Scores(user_id = user.id)
        session.add(scores)
        
        scores.dark = 0
        scores.crass = 0
        scores.stand_up = 100
        scores.satire = 0
        scores.dry = 0
        scores.sketch_imporv = 0
        scores.slapstick = 0
        scores.pardoy = 0
        
        content1 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=9FPv2toi5og").first()
        
        
        user.dislike_content = []
        
        response = self.client.get("/content")
        response = self.client.post("/content", data = {
                "content.id": "1",
                "dislike_like_vulgar":"dislike"
            })
        user = session.query(User).filter(User.email == "alice@example.com").first()
        
        dislike = [content.id for content in user.dislike_content]
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(dislike, [1])
        
        
    def testContentMarkVulgar(self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        scores = Scores(user_id = user.id)
        session.add(scores)
        
        scores.dark = 0
        scores.crass = 0
        scores.stand_up = 100
        scores.satire = 0
        scores.dry = 0
        scores.sketch_imporv = 0
        scores.slapstick = 0
        scores.pardoy = 0
        
        content1 = session.query(Content).filter(Content.link =="https://www.youtube.com/watch?v=HjLr7Duq3B8").first()
        
        response = self.client.get("/content")
        response = self.client.post("/content", data = {
                "content.id": "2",
                "dislike_like_vulgar":"vulgar"
            })
        self.assertEqual(response.status_code, 302)
        
          
        
        response = self.client.get("/content")
        
        self.assertEqual(response.status_code, 200)
        content = session.query(Content).filter(Content.link == "https://www.youtube.com/watch?v=HjLr7Duq3B8").first()
        print "Test Content Vulgar"
        print content.vulgar
        self.assertEqual(content.vulgar, 1)
        
    
    def testContentLike(self):
        
        self.simulate_login()
        user = session.query(User).filter(User.email == "alice@example.com").first()
        scores = Scores(user_id = user.id)
        session.add(scores)
        
        scores.dark = 0
        scores.crass = 0
        scores.stand_up = 99
        scores.satire = 0
        scores.dry = 0
        scores.sketch_imporv = 0
        scores.slapstick = 0
        scores.pardoy = 0
        
        
        content2 = session.query(Content).filter(Content.link == "https://www.youtube.com/watch?v=9FPv2toi5og").first()
        
        
        response = self.client.get("/content")
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post("/content", data = {
                "content.id": "1",
                "dislike_like_vulgar":"like"
            })
        
        user = session.query(User).filter(User.email == "alice@example.com").first()
        scores = session.query(Scores).filter(User.id == 1).first()
        print scores.stand_up
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(scores.stand_up, 100)
        
        
        
if __name__ == "__main__":
    unittest.main()       