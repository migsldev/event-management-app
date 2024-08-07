import click
from db import init_db, SessionLocal
from user_management import user_cli
from event_management import event_cli
from schedule_management import schedule_cli
from attendee_management import attendee_cli

@click.group()
def cli():
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized!")

cli.add_command(user_cli, name='user')
cli.add_command(event_cli, name='event')
cli.add_command(schedule_cli, name='schedule')
cli.add_command(attendee_cli, name='attendee')

if __name__ == '__main__':
    cli()
