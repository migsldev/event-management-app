import click
from sqlalchemy.orm import Session
from datetime import datetime
from db import SessionLocal
from models import Event, EventSchedule

@click.group()
def schedule_cli():
    """Event Schedule Management CLI"""
    pass

@schedule_cli.command()
@click.argument('event_id', type=int)
@click.argument('start_time')
@click.argument('end_time')
def add(event_id, start_time, end_time):
    """Add a new schedule to an event."""
    session: Session = SessionLocal()
    event = session.query(Event).get(event_id)
    if not event:
        click.echo("Event not found!")
        session.close()
        return
    start_time = datetime.fromisoformat(start_time)
    end_time = datetime.fromisoformat(end_time)
    schedule = EventSchedule(event_id=event_id, start_time=start_time, end_time=end_time)
    session.add(schedule)
    session.commit()
    session.close()
    click.echo(f"Schedule added to event {event_id}!")

@schedule_cli.command()
@click.argument('schedule_id', type=int)
@click.argument('start_time')
@click.argument('end_time')
def update(schedule_id, start_time, end_time):
    """Update an existing schedule."""
    session: Session = SessionLocal()
    schedule = session.query(EventSchedule).filter(EventSchedule.id == schedule_id).first()
    if not schedule:
        click.echo("Schedule not found!")
        session.close()
        return
    schedule.start_time = datetime.fromisoformat(start_time)
    schedule.end_time = datetime.fromisoformat(end_time)
    session.commit()
    session.close()
    click.echo(f"Schedule {schedule_id} updated!")

@schedule_cli.command()
@click.argument('schedule_id', type=int)
def remove(schedule_id):
    """Remove a schedule from an event."""
    session: Session = SessionLocal()
    schedule = session.query(EventSchedule).filter(EventSchedule.id == schedule_id).first()
    if not schedule:
        click.echo("Schedule not found!")
        session.close()
        return
    session.delete(schedule)
    session.commit()
    session.close()
    click.echo(f"Schedule {schedule_id} removed!")

@schedule_cli.command()
@click.argument('event_id', type=int)
def listschedules(event_id):
    """List all schedules for a specific event."""
    session: Session = SessionLocal()
    schedules = session.query(EventSchedule).filter(EventSchedule.event_id == event_id).all()
    session.close()
    if not schedules:
        click.echo(f"No schedules found for event {event_id}.")
        return
    for schedule in schedules:
        click.echo(f"Schedule ID: {schedule.id}, Start Time: {schedule.start_time}, End Time: {schedule.end_time}")

if __name__ == '__main__':
    schedule_cli()
