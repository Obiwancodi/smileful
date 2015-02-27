from sqlalchemy import Column, Integer, String, Text

from database import Base, engine

from flask.ext.login import UserMixin

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


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
    
    like_content = Column(Integer, ForeignKey('content.id'))
    
    
    
class Content(Base):
    __tablename__ = "content"
    
    id = Column(Integer, primary_key = True)
    link = Column(Text, nullable=False)
    genre = Column(String(128), nullable=False)