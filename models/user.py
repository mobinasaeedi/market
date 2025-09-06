from sqlalchemy import *
from extention import db,get_current_time
from flask_login import UserMixin 

class User(db.Model ,UserMixin ):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    username=Column(db.String,unique=True,nullable=False,index=True)
    password=Column(db.String,nullable=False,index=True)
    phone=Column(db.String,nullable=False,index=True)
    address=Column(db.String,nullable=False,index=True)
    date_created = Column(String(15), default = get_current_time)
   