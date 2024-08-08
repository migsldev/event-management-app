import click
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Attendee, Event

@click.group()
def attendee_cli():
    """Attendee Management CLI"""
    pass

@attendee_cli.command()
@click.argument('name')
@click.argument('event_id', type=int)
def register(name, event_id):
    """Register a new attendee to an event."""
    session: Session = SessionLocal()
    event = session.query(Event).get(event_id)
    if not event:
        click.echo("Event not found!")
        session.close()
        return
    attendee = Attendee(name=name, event_id=event_id)
    session.add(attendee)
    session.commit()
    session.close()
    click.echo(f"Attendee {name} registered to event {event_id}!")

@attendee_cli.command()
@click.argument('attendee_id', type=int)
@click.argument('name')
def update(attendee_id, name):
    """Update attendee information."""
    session: Session = SessionLocal()
    attendee = session.query(Attendee).filter(Attendee.id == attendee_id).first()
    if not attendee:
        click.echo("Attendee not found!")
        session.close()
        return
    attendee.name = name
    session.commit()
    session.close()
    click.echo(f"Attendee {attendee_id} updated!")

@attendee_cli.command()
@click.argument('attendee_id', type=int)
def remove(attendee_id):
    """Remove an attendee from an event."""
    session: Session = SessionLocal()
    attendee = session.query(Attendee).filter(Attendee.id == attendee_id).first()
    if not attendee:
        click.echo("Attendee not found!")
        session.close()
        return
    session.delete(attendee)
    session.commit()
    session.close()
    click.echo(f"Attendee {attendee_id} removed!")

@attendee_cli.command()
@click.argument('event_id', type=int)
def listattendees(event_id):
    """List all attendees for a specific event."""
    session: Session = SessionLocal()
    attendees = session.query(Attendee).filter(Attendee.event_id == event_id).all()
    session.close()
    if not attendees:
        click.echo(f"No attendees found for event {event_id}.")
        return
    for attendee in attendees:
        click.echo(f"Attendee ID: {attendee.id}, Name: {attendee.name}")

if __name__ == '__main__':
    attendee_cli()
