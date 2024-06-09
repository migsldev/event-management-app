from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from event_management.database import Base

class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    description = Column(String)
    event = relationship('Event', back_populates='schedules')
