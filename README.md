# Client Subscription Tracker

A Django-based web application for managing clients and their subscriptions. It tracks client details, subscription status, payment status, and expiry dates.

---

## Features

- Client management (Add, Edit, View)
- Subscription tracking
- Active / Expired / Expiring Soon filtering
- Paid / Unpaid tracking
- Search functionality
- Authentication (Login / Logout)
- Bootstrap UI styling
- Form validation (dates & payment)
- Flash messages

---

## Tech Stack

- Python
- Django
- SQLite
- Bootstrap 5

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sisko-Matt/client-subscription-tracker-v2.git
cd client-subscription-tracker-v2
```

### 2. Create a virtual environment

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django
```

```bash
pip install -r requirements.txt
```

### 4. Create the MySQL database

```sql
CREATE DATABASE client_subscription_tracker;
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

## Login

Use the superuser account you created above.

## Author

Felix Omondi