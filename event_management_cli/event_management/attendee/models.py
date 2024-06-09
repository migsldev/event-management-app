from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from event_management.database import Base

class Attendee(Base):
    __tablename__ = 'attendees'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship('Event', back_populates='attendees')
