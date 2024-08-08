import click
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Event, User

@click.group()
def event_cli():
    """Event Management CLI"""
    pass


@event_cli.command('create')
@click.argument('title')
@click.argument('description')
@click.argument('owner_id', type=int)
def create(title, description, owner_id):
    """Create a new event."""
    session: Session = SessionLocal()
    event = Event(title=title, description=description, owner_id=owner_id)
    session.add(event)
    session.commit()
    click.echo(f"Event '{title}' created with ID: {event.id}")
    session.close()

@event_cli.command()
@click.argument('event_id', type=int)
@click.argument('name')
@click.argument('description')
def update(event_id, name, description):
    """Update an existing event."""
    session: Session = SessionLocal()
    event = session.query(Event).filter(Event.id == event_id).first()
    if not event:
        click.echo("Event not found!")
        session.close()
        return
    event.name = name
    event.description = description
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
        click.echo(f"ID: {event.id}, Name: {event.title}, Description: {event.description}, Created by User ID: {event.owner_id}")

if __name__ == '__main__':
    event_cli()
