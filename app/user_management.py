import click
from sqlalchemy.orm import Session
from db import SessionLocal
from models import User, Event  # Assuming Event is another model in models.py

@click.group()
def user_cli():
    """User and Event Management CLI"""
    pass

@user_cli.command()
@click.argument('username')
def create(username):
    """Create a new user."""
    session: Session = SessionLocal()
    user = User(username=username)
    session.add(user)
    session.commit()
    session.close()
    click.echo(f"User {username} created!")

@user_cli.command()
@click.argument('username')
def login(username):
    """Login (check if user exists)."""
    session: Session = SessionLocal()
    user = session.query(User).filter(User.username == username).first()
    session.close()
    if user:
        click.echo(f"User {username} logged in!")
    else:
        click.echo(f"User {username} does not exist!")

@user_cli.command()
def fetch():
    """Fetch all users."""
    session: Session = SessionLocal()
    users = session.query(User).all()
    session.close()
    for user in users:
        click.echo(f"ID: {user.id}, Username: {user.username}")

@user_cli.command()
@click.argument('username')
def createevent(username):
    """Create a new event."""
    session: Session = SessionLocal()
    user = session.query(User).filter(User.username == username).first()
    if not user:
        click.echo(f"User {username} does not exist!")
        return
    event_name = click.prompt('Event name')
    event_description = click.prompt('Event description')
    event = Event(title=event_name, description=event_description, owner_id=user.id)
    session.add(event)
    session.commit()
    session.close()
    click.echo(f"Event '{event_name}' created by {username}!")

@user_cli.command()
@click.argument('event_id', type=int)
def deleteevent(event_id):
    """Delete an event."""
    session: Session = SessionLocal()
    event = session.query(Event).filter(Event.id == event_id).first()
    if event:
        session.delete(event)
        session.commit()
        click.echo(f"Event {event_id} deleted!")
    else:
        click.echo(f"Event {event_id} does not exist!")
    session.close()

@user_cli.command()
def viewavailableevents():
    """View all available events (created by user and not created by user)."""
    session: Session = SessionLocal()
    events = session.query(Event).all()
    session.close()
    for event in events:
        click.echo(f"Event: {event.title} (Created by User ID: {event.owner_id})")

@user_cli.command()
def viewallevents():
    """View all events that are happening."""
    session: Session = SessionLocal()
    events = session.query(Event).all()
    session.close()
    for event in events:
        click.echo(f"Event: {event.title} (Created by User ID: {event.owner_id})")

@user_cli.command()
@click.argument('event_id', type=int)
@click.argument('username')
def joinevent(event_id, username):
    """Join an event and show details about the event."""
    session: Session = SessionLocal()
    event = session.query(Event).filter(Event.id == event_id).first()
    if event:
        click.echo(f"Event: {event.title} (Created by User ID: {event.owner_id})")
        join = click.confirm("Would you like to join this event?")
        if join:
            # Assuming you have a mechanism to associate users with events
            # This is a placeholder
            click.echo(f"User {username} joined event {event_id}!")
        else:
            click.echo("User did not join the event.")
    else:
        click.echo(f"Event {event_id} does not exist!")
    session.close()

if __name__ == '__main__':
    user_cli()
