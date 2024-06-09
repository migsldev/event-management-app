import click
from sqlalchemy.orm import Session
from event_management.database import SessionLocal
from event_management.event import crud as event_crud
from event_management.attendee import crud as attendee_crud
from event_management.schedule import crud as schedule_crud
from event_management.user import crud as user_crud
from datetime import datetime

# Dependency Injection for Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@click.group()
def cli():
    pass

# Event Commands
@cli.group()
def event():
    pass

@event.command()
@click.argument('name')
@click.argument('date')
@click.argument('location')
def create(name, date, location):
    db = next(get_db())
    # Convert date string to datetime object
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    event = event_crud.create_event(db, name, date_obj, location)
    click.echo(f"Event created: {event.name} on {event.date} at {event.location}")

@event.command()
def list():
    db = next(get_db())
    events = event_crud.get_events(db)
    for event in events:
        click.echo(f"ID: {event.id}, Name: {event.name}, Date: {event.date}, Location: {event.location}")

# Attendee Commands
@cli.group()
def attendee():
    pass

@attendee.command()
@click.argument('name')
@click.argument('email')
@click.argument('event_id')
def register(name, email, event_id):
    db = next(get_db())
    attendee = attendee_crud.register_attendee(db, name, email, event_id)
    click.echo(f"Attendee {attendee.name} registered with email {attendee.email} for event ID {attendee.event_id}")

@attendee.command()
@click.argument('event_id')
def list(event_id):
    db = next(get_db())
    attendees = attendee_crud.get_attendees_for_event(db, event_id)
    for attendee in attendees:
        click.echo(f"ID: {attendee.id}, Name: {attendee.name}, Email: {attendee.email}, Event ID: {attendee.event_id}")

# Schedule Commands
@cli.group()
def schedule():
    pass

@schedule.command()
@click.argument('event_id')
@click.argument('start_time')
@click.argument('end_time')
@click.argument('description')
def add(event_id, start_time, end_time, description):
    db = next(get_db())
    # Convert time strings to datetime objects
    start_time_obj = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end_time_obj = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
    schedule = schedule_crud.add_schedule(db, event_id, start_time_obj, end_time_obj, description)
    click.echo(f"Schedule added: {schedule.description} from {schedule.start_time} to {schedule.end_time}")

@schedule.command()
@click.argument('event_id')
def list(event_id):
    db = next(get_db())
    schedules = schedule_crud.get_schedules_for_event(db, event_id)
    for schedule in schedules:
        click.echo(f"ID: {schedule.id}, Event ID: {schedule.event_id}, Start Time: {schedule.start_time}, End Time: {schedule.end_time}, Description: {schedule.description}")

# User Commands
@cli.group()
def user():
    pass

@user.command()
@click.argument('username')
@click.argument('password')
def create(username, password):
    db = next(get_db())
    user = user_crud.create_user(db, username, password)
    click.echo(f"User created: {user.username}")

@user.command()
def list():
    db = next(get_db())
    users = user_crud.get_users(db)
    for user in users:
        click.echo(f"ID: {user.id}, Username: {user.username}")

if __name__ == '__main__':
    cli()
