from sqlalchemy import Table, Column, Integer, String, Text

from database import Base, engine

from flask.ext.login import UserMixin

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from smileful import db




user_dislike_content_table = Table('user_dislike_content_association', Base.metadata,
                                  Column('users.id', Integer, ForeignKey('users.id')),
                                  Column('content.id', Integer, ForeignKey('content.id'))
                                  )

user_seen_table = Table('user_content_seen_association', Base.metadata,
                       Column('users.id', Integer, ForeignKey('users.id')),
                       Column('content.id', Integer, ForeignKey('content.id'))
                       )


class User(Base, UserMixin):
    __tablename__ = "users"
    
    """want_vulgar=0 means want vulgar content = 1 means do not"""
    
    id = Column(Integer, primary_key = True)
    email = Column(String(128), unique=True)
    password = Column(String(128), nullable=False)
    scores = relationship("Scores", uselist=False, backref="person")
    want_vulgar = Column(Integer, nullable=False, default=0)
      
    dislike_content = relationship("Content", secondary="user_dislike_content_association",
                                 backref = "duser")
    
    user_seen_content = relationship("Content", secondary="user_content_seen_association",
                                    backref = "seencon")  

       
class Scores(Base):
    __tablename__ = "scores"
    
    
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    dark = Column(Integer, nullable=False, default=0) 
    crass = Column(Integer, nullable=False, default=0) 
    stand_up = Column(Integer, nullable=False, default=0) 
    satire = Column(Integer, nullable=False, default=0) 
    dry = Column(Integer, nullable=False, default=0) 
    sketch_improv = Column(Integer, nullable=False, default=0)
    topical = Column(Integer, nullable=False, default=0)
    slapstick = Column(Integer, nullable=False, default=0)
    surreal = Column(Integer, nullable=False, default=0)
    pardoy = Column(Integer, nullable=False, default=0)
    
    def make_scores_dict(self):
        scores_dict = {
            "dark": self.dark,
            "crass": self.crass,
            "stand_up": self.stand_up,
            "satire": self.satire,
            "dry": self.dry,
            "sketch_improv": self.sketch_improv,
            "topical": self.topical,
            "slapstick": self.slapstick,
            "surreal": self.surreal,
            "pardoy": self.pardoy
        }
        return scores_dict
    
    
class Content(Base):
    __tablename__ = "content"
    """O in Vulgar means not Vulgar 1 means it is Vulgar"""
    
    id = Column(Integer, primary_key = True)
    link = Column(Text, nullable=False)
    genre = Column(String(128), nullable=False)
    vulgar = Column(Integer, nullable=False, default=0)
    
    def content_as_dictionary(self):
        content = {
            "id": self.id,
            "link": self.link,
            "genre": self.genre
        }
        return content
    
