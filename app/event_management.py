import click
from sqlalchemy.orm import Session
from datetime import datetime
from db import SessionLocal
from models import Event, Attendee

@click.group()
def event_cli():
    """Event and Schedule Management CLI"""
    pass

@event_cli.command('create')
@click.argument('title')
@click.argument('description')
@click.argument('start_time')
@click.argument('end_time')
@click.argument('owner_id', type=int)
def create(title, description, start_time, end_time, owner_id):
    """Create a new event with schedule."""
    session: Session = SessionLocal()
    start_time = datetime.fromisoformat(start_time)
    end_time = datetime.fromisoformat(end_time)
    event = Event(title=title, description=description, start_time=start_time, end_time=end_time, owner_id=owner_id)
    session.add(event)
    session.commit()
    
    # Access event.id before closing the session
    event_id = event.id
    
    session.close()
    click.echo(f"Event '{title}' created with ID: {event_id}")
    
@event_cli.command()
@click.argument('event_id', type=int)
@click.argument('title')
@click.argument('description')
@click.argument('start_time')
@click.argument('end_time')
def update(event_id, title, description, start_time, end_time):
    """Update an existing event and schedule."""
    session: Session = SessionLocal()
    event = session.query(Event).filter(Event.id == event_id).first()
    if not event:
        click.echo("Event not found!")
        session.close()
        return
    event.title = title
    event.description = description
    event.start_time = datetime.fromisoformat(start_time)
    event.end_time = datetime.fromisoformat(end_time)
    session.commit()
    session.close()
    click.echo(f"Event {event_id} updated!")

@event_cli.command()
@click.argument('event_id', type=int)
def delete(event_id):
    """Delete an event."""
    session: Session = SessionLocal()
    event = session.query(Event).filter(Event.id == event_id).first()
    if not event:
        click.echo("Event not found!")
        session.close()
        return
    session.delete(event)
    session.commit()
    session.close()
    click.echo(f"Event {event_id} deleted!")

@event_cli.command()
def listevents():
    """List all events with details."""
    session: Session = SessionLocal()
    events = session.query(Event).all()
    session.close()
    if not events:
        click.echo("No events found.")
        return
    for event in events:
        click.echo(f"ID: {event.id}, Title: {event.title}, Description: {event.description}, "
                   f"Start Time: {event.start_time}, End Time: {event.end_time}, Created by User ID: {event.owner_id}")

if __name__ == '__main__':
    event_cli()
