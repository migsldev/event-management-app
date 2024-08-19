import click
from db import init_db
from event_management import event_cli
from attendee_management import attendee_cli
from user_management import user_cli

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
cli.add_command(attendee_cli, name='attendee')

if __name__ == '__main__':
    cli()
