import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgres://ssckesofzxuvhe:0R4iBHYpKRrrK08yRJAm8UvxRA@ec2-54-163-234-163.compute-1.amazonaws.com:5432/d9h0o4d9300dlm"
    DEBUG = True
    SECRET_KEY = os.environ.get("SMILEFUL_SECRET_KEY", "")
    
class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://:@localhost:5432/smileful_test"
    DEBUG = True
    SECRET_KEY = "Not secret"