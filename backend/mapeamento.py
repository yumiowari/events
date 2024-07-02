# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Classification(Base):
    __tablename__ = 'classifications'

    id = Column(String(20), primary_key=True)
    name = Column(String(50), nullable=False)
    segmentid = Column(String(20), nullable=False)
    segmentname = Column(String(50), nullable=False)


class Venues(Base):
    __tablename__ = 'venues'

    id = Column(String(20), primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(Text)
    postalcode = Column(Integer, nullable=False)
    timezone = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    state = Column(String(20), nullable=False)
    country = Column(String(30), nullable=False)
    address = Column(String(50))


class Attractions(Base):
    __tablename__ = 'attractions'

    id = Column(String(20), primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(Text)
    classificationsid = Column(ForeignKey('classifications.id'))

    classification = relationship('Classifications')


class Events(Base):
    __tablename__ = 'events'

    id = Column(String(20), primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(Text)
    startdatesale = Column(Date)
    enddatesale = Column(Date)
    startdateevent = Column(Date)
    timezone = Column(String(20))
    minprice = Column(Float(53))
    maxprice = Column(Float(53))
    promoter = Column(String(20))
    venueid = Column(ForeignKey('venues.id'))
    classificationsid = Column(ForeignKey('classifications.id'))

    classification = relationship('Classifications')
    venue = relationship('Venues')


class Market(Base):
    __tablename__ = 'market'

    id = Column(String(70), primary_key=True)
    market = Column(String(50), nullable=False)
    venueid = Column(ForeignKey('venues.id'), nullable=False)

    venue = relationship('Venues')


class VenueAlia(Base):
    __tablename__ = 'venue_alias'

    alias = Column(String(50), primary_key=True)
    venueid = Column(ForeignKey('venues.id'), nullable=False)

    venue = relationship('Venues')


class VenueImage(Base):
    __tablename__ = 'venue_image'

    image = Column(Text, primary_key=True)
    venueid = Column(ForeignKey('venues.id'), nullable=False)

    venue = relationship('Venues')


class AttractionImage(Base):
    __tablename__ = 'attraction_image'

    image = Column(Text, primary_key=True)
    attractionid = Column(ForeignKey('attractions.id'), nullable=False)

    attraction = relationship('Attractions')


class EventAttraction(Base):
    __tablename__ = 'event_attraction'

    id = Column(String(40), primary_key=True)
    eventid = Column(ForeignKey('events.id'), nullable=False)
    attractionid = Column(ForeignKey('attractions.id'), nullable=False)

    attraction = relationship('Attractions')
    event = relationship('Events')


class EventImage(Base):
    __tablename__ = 'event_image'

    image = Column(Text, primary_key=True)
    eventid = Column(ForeignKey('events.id'), nullable=False)

    event = relationship('Events')
