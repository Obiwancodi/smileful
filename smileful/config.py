import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://:@localhost:5432/smileful"
    DEBUG = True
    SECRET_KEY = os.environ.get("SMILEFUL_SECRET_KEY", "")
    
class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://:@localhost:5432/smileful_test"
    DEBUG = False
    SECRET_KEY = "Not secret"
    
    