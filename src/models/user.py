"""
Define the User model
"""
from . import db
from sqlalchemy import Column, String, Boolean, Integer, DateTime
from sqlalchemy.dialects.postgresql import JSON

from .mixins import BaseModel


class User(db.Model, BaseModel):
    """ The User model """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_uuid = Column(String)
    phone_number = Column(String(14))
    pin = Column(String)
    email = Column(String)
    additional_data = Column(JSON, default=None)
    first_name = Column(String(32))
    last_name = Column(String(32))
    middle_name = Column(String(32))
    country = Column(String(32))
    city = Column(String(32))
    state = Column(String(32))
    dob = Column(String(16))
