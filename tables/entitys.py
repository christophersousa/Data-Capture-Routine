from sqlalchemy import Column, Integer, String, ForeignKey, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Deals(Base):
  __tablename__ = 'deal'
  id = Column(UUID, primary_key=True, nullable=False)
  deal_rd_id = Column(String, nullable=False)
  name  = Column(String)
  pipeline = Column(String)
  stage = Column(String)
  date_create = Column(String)
  date_update = Column(String)
  rating_id = Column(UUID, nullable=False)

class Rating(Base):
  __tablename__ = 'rating'
  id = Column(UUID, primary_key=True, nullable=False)
  rank = Column(Integer, nullable=False)
  name  = Column(String)
  date_create = Column(String)
  date_update = Column(String)

class Resume(Base):
  __tablename__ = 'resume'
  id = Column(UUID, primary_key=True, nullable=False)
  text = Column(String)
  report  = Column(String)
  date_create = Column(String)
  date_update = Column(String)
  deal_id = Column(UUID, nullable=False)

class Address(Base):
  __tablename__ = 'adress'
  id = Column(UUID, primary_key=True, nullable=False)
  cep = Column(String)
  state  = Column(String)
  state_code  = Column(String)
  lat  = Column(String)
  lon  = Column(String)
  date_create = Column(String)
  date_update = Column(String)

class Organization(Base):
  __tablename__ = 'organization'
  id = Column(UUID, primary_key=True, nullable=False)
  organization_rd_id = Column(String)
  name  = Column(String)
  date_create = Column(String)
  date_update = Column(String)
  document = Column(String)