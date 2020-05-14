from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()
#class Developer(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(20))

    #def __init__(self, name):
     #   self.name = name

    #def serialize(self):
     #   return {"id": self.id,
      #          "name": self.name}


class Puppy(Base):
    __tablename__ = 'puppy'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))

    def __init__(self,name,description):
        self.name = name
        self.description = description
        

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
       		'id': self.id,
           'name': self.name,
           'description' : self.description
       }

engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)