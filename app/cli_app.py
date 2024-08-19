import click
import inquirer
from db import init_db, SessionLocal
from models import Event, Attendee, User
from datetime import datetime


def main_menu():
    questions = [
        inquirer.List('option',
                      message="Choose an action",
                      choices=[
                          'Initialize Database',
                          'Manage Events',
                          'Manage Attendees',
                          'Manage Users',
                          'Exit'
                      ])
    ]
    answer = inquirer.prompt(questions)
    return answer['option']


def event_menu():
    questions = [
        inquirer.List('option',
                      message="Event Management - Choose an action",
                      choices=[
                          'Create Event',
                          'Update Event',
                          'Delete Event',
                          'List Events',
                          'Back to Main Menu'
                      ])
    ]
    answer = inquirer.prompt(questions)
    return answer['option']


def attendee_menu():
    questions = [
        inquirer.List('option',
                      message="Attendee Management - Choose an action",
                      choices=[
                          'Register Attendee',
                          'Update Attendee',
                          'Remove Attendee',
                          'List Attendees',
                          'Back to Main Menu'
                      ])
    ]
    answer = inquirer.prompt(questions)
    return answer['option']


def user_menu():
    questions = [
        inquirer.List('option',
                      message="User Management - Choose an action",
                      choices=[
                          'Create User',
                          'Fetch Users',
                          'Back to Main Menu'
                      ])
    ]
    answer = inquirer.prompt(questions)
    return answer['option']


def create_event():
    session = SessionLocal()
    title = click.prompt("Enter event title")
    description = click.prompt("Enter event description")
    start_time = click.prompt("Enter start time (YYYY-MM-DDTHH:MM:SS)")
    end_time = click.prompt("Enter end time (YYYY-MM-DDTHH:MM:SS)")
    owner_id = click.prompt("Enter owner ID", type=int)
    event = Event(title=title, description=description,
                  start_time=datetime.fromisoformat(start_time),
                  end_time=datetime.fromisoformat(end_time), owner_id=owner_id)
    session.add(event)
    session.commit()
    session.close()
    click.echo(f"Event '{title}' created")


def update_event():
    session = SessionLocal()
    event_id = click.prompt("Enter event ID to update", type=int)
    event = session.query(Event).filter(Event.id == event_id).first()
    if not event:
        click.echo("Event not found!")
        session.close()
        return
    event.title = click.prompt("Enter new event title", default=event.title)
    event.description = click.prompt("Enter new event description", default=event.description)
    event.start_time = datetime.fromisoformat(click.prompt("Enter new start time (YYYY-MM-DDTHH:MM:SS)", default=event.start_time.isoformat()))
    event.end_time = datetime.fromisoformat(click.prompt("Enter new end time (YYYY-MM-DDTHH:MM:SS)", default=event.end_time.isoformat()))
    session.commit()
    session.close()
    click.echo(f"Event {event_id} updated!")


def delete_event():
    session = SessionLocal()
    event_id = click.prompt("Enter event ID to delete", type=int)
    event = session.query(Event).filter(Event.id == event_id).first()
    if not event:
        click.echo("Event not found!")
        session.close()
        return
    session.delete(event)
    session.commit()
    session.close()
    click.echo(f"Event {event_id} deleted!")


def list_events():
    session = SessionLocal()
    events = session.query(Event).all()
    session.close()
    if not events:
        click.echo("No events found.")
        return
    for event in events:
        click.echo(f"ID: {event.id}, Title: {event.title}, Description: {event.description}, "
                   f"Start Time: {event.start_time}, End Time: {event.end_time}, Created by User ID: {event.owner_id}")


def create_user():
    session = SessionLocal()
    username = click.prompt("Enter username")
    user = User(username=username)
    session.add(user)
    session.commit()
    session.close()
    click.echo(f"User {username} created!")


def fetch_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    for user in users:
        click.echo(f"ID: {user.id}, Username: {user.username}")


def register_attendee():
    session = SessionLocal()
    name = click.prompt("Enter attendee name")
    event_id = click.prompt("Enter event ID", type=int)
    attendee = Attendee(name=name, event_id=event_id)
    session.add(attendee)
    session.commit()
    session.close()
    click.echo(f"Attendee {name} registered to event {event_id}!")


def update_attendee():
    session = SessionLocal()
    attendee_id = click.prompt("Enter attendee ID to update", type=int)
    attendee = session.query(Attendee).filter(Attendee.id == attendee_id).first()
    if not attendee:
        click.echo("Attendee not found!")
        session.close()
        return
    attendee.name = click.prompt("Enter new attendee name", default=attendee.name)
    session.commit()
    session.close()
    click.echo(f"Attendee {attendee_id} updated!")


def remove_attendee():
    session = SessionLocal()
    attendee_id = click.prompt("Enter attendee ID to remove", type=int)
    attendee = session.query(Attendee).filter(Attendee.id == attendee_id).first()
    if not attendee:
        click.echo("Attendee not found!")
        session.close()
        return
    session.delete(attendee)
    session.commit()
    session.close()
    click.echo(f"Attendee {attendee_id} removed!")


def list_attendees():
    session = SessionLocal()
    event_id = click.prompt("Enter event ID to list attendees", type=int)
    attendees = session.query(Attendee).filter(Attendee.event_id == event_id).all()
    session.close()
    if not attendees:
        click.echo(f"No attendees found for event {event_id}.")
        return
    for attendee in attendees:
        click.echo(f"Attendee ID: {attendee.id}, Name: {attendee.name}")


def run_cli():
    while True:
        choice = main_menu()

        if choice == 'Initialize Database':
            init_db()
            click.echo("Database initialized!")
        elif choice == 'Manage Events':
            while True:
                event_choice = event_menu()
                if event_choice == 'Create Event':
                    create_event()
                elif event_choice == 'Update Event':
                    update_event()
                elif event_choice == 'Delete Event':
                    delete_event()
                elif event_choice == 'List Events':
                    list_events()
                elif event_choice == 'Back to Main Menu':
                    break
        elif choice == 'Manage Attendees':
            while True:
                attendee_choice = attendee_menu()
                if attendee_choice == 'Register Attendee':
                    register_attendee()
                elif attendee_choice == 'Update Attendee':
                    update_attendee()
                elif attendee_choice == 'Remove Attendee':
                    remove_attendee()
                elif attendee_choice == 'List Attendees':
                    list_attendees()
                elif attendee_choice == 'Back to Main Menu':
                    break
        elif choice == 'Manage Users':
            while True:
                user_choice = user_menu()
                if user_choice == 'Create User':
                    create_user()
                elif user_choice == 'Fetch Users':
                    fetch_users()
                elif user_choice == 'Back to Main Menu':
                    break
        elif choice == 'Exit':
            click.echo("Exiting the application.")
            break


if __name__ == '__main__':
    run_cli()
