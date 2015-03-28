import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgres://xnhxsialjqhqoo:IagOEd3DJm2jMgPmG1F06HsVWH@ec2-23-21-187-45.compute-1.amazonaws.com:5432/d3dpg3es5rknub"
    DEBUG = True
    SECRET_KEY = os.environ.get("SMILEFUL_SECRET_KEY", "")
    
class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://:@localhost:5432/smileful_test"
    DEBUG = True
    SECRET_KEY = "Not secret"