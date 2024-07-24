#!/bin/python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship,aliased
from sqlalchemy.sql import func
from sqlalchemy import Table, Text




sqlalchemy.__version__ 

engine = create_engine('mysql://razaoul:Razor8617.@localhost/hbtn_0d_tvshows', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname,\
                                                                    self.nickname)

User.__table__ 
Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
ed_user.name
ed_user.nickname
str(ed_user.id)

Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

session.dirty

session.new  

session.commit()

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

User.addresses = relationship("Address", \
                              order_by=Address.id,\
                                  back_populates="user")

Base.metadata.create_all(engine)

jack = User(name='jack', fullname='Jack Bean', nickname='gjffdd')
jack.addresses

jack.addresses = [Address(email_address='jack@google.com'),\
                  Address(email_address='j25@yahoo.com')\
                    ]
session.add(jack)
session.commit()

stmt = session.query(Address.user_id, func.count('*').\
        label('address_count')).\
        group_by(Address.user_id).subquery()
for u, count in session.query(User, stmt.c.address_count).\
    outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id):
    print(u, count)
    
stmt = session.query(Address).\
                filter(Address.email_address != 'j25@yahoo.com').\
                subquery()
adalias = aliased(Address, stmt)
for user, address in session.query(User, adalias).\
        join(adalias, User.addresses):
    print(user)
    print(address)
session.delete(jack)
session.query(User).filter_by(name='jack').count()
session.close()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    addresses = relationship("Address", back_populates='user',\
                             cascade="all, delete, delete-orphan")
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (\
           self.name, self.fullname, self.nickname)
    
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
jack = session.query(User).get(5)
del jack.addresses[1]
session.query(Address).filter(\
    Address.email_address.in_(['jack@google.com', 'j25@yahoo.com'])).\
        count()
# association table
post_keywords = Table('post_keywords', Base.metadata,\
                      Column('post_id', ForeignKey('posts.id'), primary_key=True),\
                        Column('keyword_id', ForeignKey('keywords.id'), primary_key=True)\
                            )
class BlogPost(Base):
   __tablename__ = 'posts'
   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('users.id'))
   headline = Column(String(255), nullable=False)
   body = Column(Text)
   # many to many BlogPost<->Keyword
   keywords = relationship('Keyword',\
                           secondary=post_keywords,\
                               back_populates='posts')
   def __init__(self, headline, body, author):
       self.author = author
       self.headline = headline
       self.body = body
   def __repr__(self):
       return "BlogPost(%r, %r, %r)" % \
           (self.headline, self.body, self.author)

class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False, unique=True)
    posts = relationship('BlogPost',\
                         secondary=post_keywords,\
                            back_populates='keywords')
    def __init__(self, keyword):
        self.keyword = keyword
BlogPost.author = relationship(User, back_populates="posts")
User.posts = relationship(BlogPost, back_populates="author", lazy="dynamic")
Base.metadata.create_all(engine)
wendy = session.query(User).\
                 filter_by(name='wendy').\
                 first()
post = BlogPost("Wendy's Blog Post", "This is a test", wendy)
session.add(post)
post.keywords.append(Keyword('wendy'))
post.keywords.append(Keyword('firstpost'))

session.query(BlogPost).\
             filter(BlogPost.keywords.any(keyword='firstpost')).\
             all()
session.query(BlogPost).\
             filter(BlogPost.author==wendy).\
             all()
wendy.posts.\
         filter(BlogPost.keywords.any(keyword='firstpost')).\
         all()