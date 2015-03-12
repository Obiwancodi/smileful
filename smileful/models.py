from sqlalchemy import Table, Column, Integer, String, Text

from database import Base, engine

from flask.ext.login import UserMixin

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

user_like_content_table = Table('user_content_like_association', Base.metadata,
                          Column('users.id', Integer, ForeignKey('users.id')),
                          Column('content.id', Integer, ForeignKey('content.id'))
                          )

user_dislike_content_table = Table('user_dislike_content_association', Base.metadata,
                                  Column('users.id', Integer, ForeignKey('users.id')),
                                  Column('content.id', Integer, ForeignKey('content.id'))
                                  )


class User(Base, UserMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    email = Column(String(128), unique=True)
    password = Column(String(128), nullable=False)
    
    dark = Column(Integer, nullable=False, default=0)
    crass = Column(Integer, nullable=False, default=0)
    stand_up = Column(Integer, nullable=False, default=0)
    satire = Column(Integer, nullable=False, default=0)
    dry = Column(Integer, nullable=False, default=0)
    animated = Column(Integer, nullable=False, default=0)
    topical = Column(Integer, nullable=False, default=0)
    slapstick = Column(Integer, nullable=False, default=0)
    surreal = Column(Integer, nullable=False, default=0)
    situational = Column(Integer, nullable=False, default=0)
    improv = Column(Integer, nullable=False, default=0)
    
    like_content = relationship("Content", secondary="user_content_like_association",
                               backref="luser")
    dislike_content = relationship("Content", secondary="user_dislike_content_association",
                                  backref = "duser")
    
    def calculate_score(self):
        total_score = self.dark + self.crass + self.stand_up + self.satire + self.dry + self.animated + self.topical + self.slapstick + self.surreal + self.situational + self.improv
        
        self.dark_score = self.dark/total_score * 100
        crass_score = self.crass/total_score * 100
        stand_up_score = self.stand_up/total_score * 100
        satire_score = self.satire/total_score * 100
        dry_score = self.dry/total_score * 100
        animated_score = self.animated/total_score * 100
        topical_score = self.topical/total_score * 100
        slapstick_score = self.slapstick/total_score * 100
        surreal_score = self.surreal/total_score * 100
        situational_score = self.situational/total_score * 100
        improv_score = self.improv/total_score * 100
        
        



        
class Content(Base):
    __tablename__ = "content"
    
    id = Column(Integer, primary_key = True)
    link = Column(Text, nullable=False)
    genre = Column(String(128), nullable=False)
    
    def content_as_dictionary(self):
        content = {
            "id": self.id,
            "link": self.link,
            "genre": self.genre
        }
        return content
    
