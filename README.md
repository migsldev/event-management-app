# Event Management CLI Application

## Project Description

The Event Management CLI application is a Command Line Interface (CLI) tool designed for managing events and attendees. This application allows users to create and manage events, register attendees, and keep track of event details. The project utilizes SQLAlchemy ORM for database interactions, and Click or Fire for CLI tasks, adhering to best practices for environment configuration, package structure, and CLI design.

## Features

### 1. Event Management
- Create, update, and delete events.
- List all events with details.

### 2. Attendee Management
- Register attendees to events.
- Update and remove attendee information.
- List all attendees for a specific event.

### 3. Event Schedule Management
- Add, update, and remove schedules for events.
- List schedules for specific events.

### 4. User Management
- Login (check if user exists or not).
- Fetch users.
- Create users by a user.
- Create event.
- Delete event.
- View available events (created by user and not created by user).
- View all events that are happening.
- Join events.
  - Show details about the event.
  - Prompt "would you like to join event".

## Getting Started

### Prerequisites
- Python 3.10
- Pipenv for virtual environment and dependency management

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/event-management-cli-app.git
    cd event-management-cli-app
    ```

2. **Set up the virtual environment:**

    ```bash
    pipenv install
    ```

3. **Activate the virtual environment:**

    ```bash
    pipenv shell
    ```

4. **Set up the database:**

    **Initialize Alembic (if not already done):**

    ```bash
    alembic init migrations
    ```

    **Generate the initial migration:**

    ```bash
    alembic revision --autogenerate -m "Create Initial models"
    ```

    **Apply the migration:**

    ```bash
    alembic upgrade head
    ```

### Usage

Run the CLI application:

```bash
python app/cli.py
