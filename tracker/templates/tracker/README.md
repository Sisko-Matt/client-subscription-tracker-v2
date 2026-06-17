# Client Subscription Tracker

A Django application for managing clients and tracking subscriptions.

## Features

- Add, edit, and view clients
- Add subscriptions
- Dashboard statistics
- Search clients
- Filter subscriptions
- SQLite database

## Technologies Used

- Python
- Django
- SQLite
- Bootstrap

## Installation

### Clone the repository

git clone <repository-url>

### Navigate into project

cd client-subscription-tracker

### Create virtual environment

python -m venv env

### Activate virtual environment

env\Scripts\activate

### Install dependencies

pip install -r requirements.txt

### Run migrations

python manage.py migrate

### Create superuser

python manage.py createsuperuser

### Run server

python manage.py runserver

## Implemented Requirements

### Client Management

- Add client
- Edit client
- View clients

### Subscription Tracking

- Add subscriptions
- Active subscriptions
- Expired subscriptions
- Expiring within 7 days

### Dashboard

- Total clients
- Active subscriptions
- Expired subscriptions
- Expiring soon
- Unpaid subscriptions

### Search and Filter

- Search by name
- Search by email
- Search by phone number
- Search by business name
- Filter subscriptions by payment status