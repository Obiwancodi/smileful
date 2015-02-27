import os
import unittest
from urlparse import urlparse


from werkzeug.security import generate_password_hash

os.environ["CONFIG_PATH"] = "smileful.config.TestingConfig"

from blog import app
from blog import models
from blog.database import Base, engine, session


class TestViews(unittest.TestCase):
    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)

        # Create an example user
        self.user = models.User(name="Alice", email="alice@example.com",
                                password=generate_password_hash("test"))
        session.add(self.user)
        session.commit()

    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)