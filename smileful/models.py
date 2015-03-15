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
    
    dark_score = Column(Integer, nullable=False, default=0)
    crass_score = Column(Integer, nullable=False, default=0)
    stand_up_score = Column(Integer, nullable=False, default=0)
    satire_score = Column(Integer, nullable=False, default=0)
    dry_score = Column(Integer, nullable=False, default=0)
    animated_score = Column(Integer, nullable=False, default=0)
    topical_score = Column(Integer, nullable=False, default=0)
    slapstick_score = Column(Integer, nullable=False, default=0)
    surreal_score = Column(Integer, nullable=False, default=0)
    situational_score = Column(Integer, nullable=False, default=0)
    improv_score = Column(Integer, nullable=False, default=0)
    
    dark_location = Column(Integer, nullable=False, default=0)
    crass_location = Column(Integer, nullable=False, default=0)
    stand_up_location = Column(Integer, nullable=False, default=0)
    satire_location = Column(Integer, nullable=False, default=0)
    dry_location = Column(Integer, nullable=False, default=0)
    animated_location = Column(Integer, nullable=False, default=0)
    topical_location = Column(Integer, nullable=False, default=0)
    slapstick_location = Column(Integer, nullable=False, default=0)
    surreal_location = Column(Integer, nullable=False, default=0)
    situational_location = Column(Integer, nullable=False, default=0)
    improv_location = Column(Integer, nullable=False, default=0)
    
    
    like_content = relationship("Content", secondary="user_content_like_association",
                               backref="luser")
    dislike_content = relationship("Content", secondary="user_dislike_content_association",
                                  backref = "duser")
    
              
    def calulate_dict_score(self):
        total_score = self.dark + self.crass + self.stand_up +self.satire + self.dry + self.animated + self.topical + self.slapstick + self.surreal + self.situational +         self.improv
        
        self.dark_score = float(self.dark)/(total_score) * 100
        self.crass_score = float(self.crass)/(total_score) * 100
        self.stand_up_score = float(self.stand_up)/(total_score) * 100
        self.satire_score = float(self.satire)/(total_score) * 100
        self.dry_score = float(self.dry)/(total_score) * 100
        self.animated_score = float(self.animated)/(total_score) * 100
        self.topical_score = float(self.topical)/(total_score) * 100
        self.slapstick_score = float(self.slapstick)/(total_score) * 100
        self.surreal_score = float(self.surreal)/(total_score) * 100
        self.situational_score = float(self.situational)/(total_score) * 100
        self.improv_score = float(self.improv)/(total_score) * 100
        
        

    def calulate_location(self):
        self.dark_location = self.dark_score
        self.crass_location = self.dark_location + self.crass_score
        self.stand_up_location = self.crass_location + self.stand_up_score
        self.satire_location = self.stand_up_location + self.satire_score
        self.dry_location = self.satire_location + self.dry_score
        self.animated_location = self.dry_location + self.animated_score
        self.topical_location = self.animated_location + self.topical_score
        self.slapstick_location = self.topical_location + self.slapstick_score
        self.surreal_location = self.slapstick_location + self.surreal_score
        self.situational_location = self.surreal_location + self.situational_score
        self.improv_location = self.situational_location + self.improv_score
        
    def score_dict(self):
        location = (
                ("dark", self.dark_location),
                ("crass", self.crass_location),
                ("stand_up", self.stand_up_location),
                ("satire", self.satire_location),
                ("dry", self.dry_location),
                ("animated", self.animated_location),
                ("topical", self.topical_location),
                ("slapstick", self.slapstick_location),
                ("surreal", self.surreal_location),
                ("situational", self.situational_location),
                ("improv", self.improv_location)
                
            )
        return location
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
    
