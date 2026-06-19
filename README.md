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

### 1. Clone repository
```bash
git clone https://github.com/Sisko-Matt/client-subscription-tracker-v2.git
cd client-subscription-tracker-v2
2. Create virtual environment
python -m venv env
env\Scripts\activate
3. Install dependencies
pip install django
4. Run migrations
python manage.py migrate
5. Create superuser
python manage.py createsuperuser
6. Run server
python manage.py runserver
Login Details

Use the superuser account created above.

Author

Felix Omondi