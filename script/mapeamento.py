# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Classification(Base):
    __tablename__ = 'classifications'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    segmentid = Column(Text, nullable=False)
    segmentname = Column(Text, nullable=False)


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text)
    postalcode = Column(Text, nullable=False)
    timezone = Column(Text, nullable=False)
    city = Column(Text, nullable=False)
    state = Column(Text, nullable=False)
    country = Column(Text, nullable=False)
    address = Column(Text)


class Attraction(Base):
    __tablename__ = 'attractions'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text)
    classificationsid = Column(ForeignKey('classifications.id'))

    classification = relationship('Classification')


class Event(Base):
    __tablename__ = 'events'

    id = Column(Text, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text)
    startdatesale = Column(Date)
    enddatesale = Column(Date)
    startdateevent = Column(Date)
    timezone = Column(Text)
    minprice = Column(Float(53))
    maxprice = Column(Float(53))
    promoter = Column(Text)
    venueid = Column(ForeignKey('venues.id'))
    classificationsid = Column(ForeignKey('classifications.id'))

    classification = relationship('Classification')
    venue = relationship('Venue')


class Market(Base):
    __tablename__ = 'market'

    id = Column(Text, primary_key=True)
    market = Column(Text)
    venueid = Column(ForeignKey('venues.id'))

    venue = relationship('Venue')


class VenueAlia(Base):
    __tablename__ = 'venue_alias'

    alias = Column(Text, primary_key=True)
    venueid = Column(ForeignKey('venues.id'))

    venue = relationship('Venue')


class VenueImage(Base):
    __tablename__ = 'venue_image'

    image = Column(Text, primary_key=True)
    venueid = Column(ForeignKey('venues.id'))

    venue = relationship('Venue')


class AttractionImage(Base):
    __tablename__ = 'attraction_image'

    image = Column(Text, primary_key=True)
    attractionid = Column(ForeignKey('attractions.id'))

    attraction = relationship('Attraction')


class EventAttraction(Base):
    __tablename__ = 'event_attraction'

    id = Column(Text, primary_key=True)
    eventid = Column(ForeignKey('events.id'))
    attractionid = Column(ForeignKey('attractions.id'))

    attraction = relationship('Attraction')
    event = relationship('Event')


class EventImage(Base):
    __tablename__ = 'event_image'

    image = Column(Text, primary_key=True)
    eventid = Column(ForeignKey('events.id'))

    event = relationship('Event')
