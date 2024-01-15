from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, ForeignKey
from sqlalchemy.orm import relationship, class_mapper
from sqlalchemy.ext.declarative import declarative_base
import uuid
Base = declarative_base()
#  Tables

class Deals(Base):
  __tablename__ = 'deal'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
  deal_rd_id = Column(String, nullable=False)
  name  = Column(String)
  pipeline = Column(String)
  stage = Column(String)
  date_create = Column(String)
  date_update = Column(String)
  closed_at = Column(String)
  rating_id = Column(UUID(as_uuid=True))
  def as_dict(self):
        return {column.key: getattr(self, column.key) for column in class_mapper(self.__class__).mapped_table.c}

class Rating(Base):
  __tablename__ = 'rating'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
  rank = Column(Integer, nullable=False)
  name  = Column(String)
  date_create = Column(String)
  date_update = Column(String)

class Resume(Base):
  __tablename__ = 'resume'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
  text = Column(String)
  report  = Column(String)
  date_create = Column(String)
  date_update = Column(String)
  deal_id = Column(UUID(as_uuid=True))

class Address(Base):
  __tablename__ = 'address'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
  cep = Column(String)
  state  = Column(String)
  state_code  = Column(String)
  lat  = Column(String)
  lon  = Column(String)
  date_create = Column(String)
  date_update = Column(String)
  def as_dict(self):
        return {column.key: getattr(self, column.key) for column in class_mapper(self.__class__).mapped_table.c}

class Organization(Base):
  __tablename__ = 'organization'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
  organization_rd_id = Column(String, unique=True, nullable=False)
  name  = Column(String)
  date_create = Column(String)
  date_update = Column(String)
  document = Column(String)
  # Correção na definição da relação
  addresses = relationship('OrganizationAddressRl', back_populates='organization', cascade='all, delete-orphan')
  contacts = relationship('OrganizationContactRl', back_populates='organization', cascade='all, delete-orphan')
  deals = relationship('OrganizationDealsRl', back_populates='organization', cascade='all, delete-orphan')
  def as_dict(self):
        return {column.key: getattr(self, column.key) for column in class_mapper(self.__class__).mapped_table.c}

class Contact(Base):
  __tablename__ = 'contact'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
  contact_rd_id = Column(String, unique=True, nullable=False)
  name  = Column(String)
  phone = Column(String)
  email = Column(String)
  date_create = Column(String)
  date_update = Column(String)
  def as_dict(self):
        return {column.key: getattr(self, column.key) for column in class_mapper(self.__class__).mapped_table.c}

#  Table relationship
  
#  Organization
class OrganizationAddressRl(Base):
  __tablename__ = 'organization_address_rl'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
  address_id = Column(UUID(as_uuid=True), ForeignKey('address.id'))
  organization_id = Column(UUID(as_uuid=True), ForeignKey('organization.id'))
  is_active = Column(Boolean)
  date_create = Column(String)
  date_update = Column(String)
  # Relations
  organization = relationship('Organization', back_populates='addresses')
  address = relationship('Address') 

class OrganizationContactRl(Base):
  __tablename__ = 'organization_contact_rl'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
  organization_id = Column(UUID(as_uuid=True), ForeignKey('organization.id'))
  contact_id = Column(UUID(as_uuid=True), ForeignKey('contact.id'))
  is_active = Column(Boolean)
  date_create = Column(String)
  date_update = Column(String)
  # Relations
  organization = relationship('Organization', back_populates='contacts')
  contact = relationship('Contact') 

class OrganizationDealsRl(Base):
  __tablename__ = 'organization_deal_rl'
  id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
  organization_id = Column(UUID(as_uuid=True), ForeignKey('organization.id'))
  deal_id = Column(UUID(as_uuid=True), ForeignKey('deal.id'))
  is_active = Column(Boolean)
  date_create = Column(String)
  date_update = Column(String)
   # Relations
  organization = relationship('Organization', back_populates='deals')
  deal = relationship('Deals')

# #  User
# class UserAddressRl(Base):
#   __tablename__ = 'user_address_rl'
#   address_id = Column(UUID(as_uuid=True), ForeignKey('address.id'))
#   contact_id = Column(UUID(as_uuid=True), ForeignKey('contact.id'))
#   is_active = Column(Boolean)
#   date_create = Column(String)
#   date_update = Column(String)
#   address = relationship("Address", back_populates="address")
#   contact = relationship("Contact", back_populates="contact")

# class UserDealRl(Base):
#   __tablename__ = 'user_address_rl'
#   user_id = Column(UUID(as_uuid=True), nullable=False)
#   deal_id = Column(UUID(as_uuid=True), nullable=False)
#   is_active = Column(Boolean)
#   date_create = Column(String)
#   date_update = Column(String)