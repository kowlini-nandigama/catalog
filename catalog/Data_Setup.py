import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    picture = Column(String(300))


class MedicineCompanyName(Base):
    __tablename__ = 'medicinecompanyname'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="medicinecompanyname")

    @property
    def serialize(self):
        """Return objects data in easily serializeable formats"""
        return {
            'name': self.name,
            'id': self.id
        }


class MedicineName(Base):
    __tablename__ = 'medicinename'
    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)
    medicinetype = Column(String(150))
    price = Column(String(10))
    description = Column(String(250))
    date = Column(DateTime, nullable=False)
    medicinecompanynameid = Column(
        Integer, ForeignKey('medicinecompanyname.id'))
    medicinecompanyname = relationship(
        MedicineCompanyName, backref=backref(
            'medicinename', cascade='all, delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref="medicinename")

    @property
    def serialize(self):
        """Return objects data in easily serializeable formats"""
        return {
            'name': self. name,
            'medicinetype': self. medicinetype,
            'price': self. price,
            'description': self. description,
            'date': self. date,
            'id': self. id
        }

engin = create_engine('sqlite:///medicines.db')
Base.metadata.create_all(engin)
