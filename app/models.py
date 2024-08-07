from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="events")

class EventSchedule(Base):
    __tablename__ = 'event_schedules'

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    start_time = Column(DateTime, index=True)
    end_time = Column(DateTime, index=True)

    event = relationship("Event", back_populates="schedules")

class Attendee(Base):
    __tablename__ = 'attendees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))

    event = relationship("Event", back_populates="attendees")

User.events = relationship("Event", order_by=Event.id, back_populates="owner")
Event.schedules = relationship("EventSchedule", order_by=EventSchedule.id, back_populates="event")
Event.attendees = relationship("Attendee", order_by=Attendee.id, back_populates="event")
