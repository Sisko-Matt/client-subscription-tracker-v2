# Client Subscription Tracker

A Django-based web application for managing clients and their subscriptions. The system allows tracking of client details, subscription status, payment status, and expiry dates.

---

## Features

- Client management (Add, Edit, List)
- Subscription management
- Subscription status tracking (Active, Expired, Expiring Soon)
- Payment tracking (Paid / Unpaid)
- Search functionality for clients
- Authentication system (Login/Logout)
- Bootstrap-based responsive UI
- Form validation (date and payment validation)
- Flash messages for user feedback

---

## Tech Stack

- Python 3.x
- Django 6.x
- SQLite (default database)
- Bootstrap 5

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Sisko-Matt/client-subscription-tracker-v2.git
cd client-subscription-tracker-v2
2. Create virtual environment
python -m venv env
env\Scripts\activate   # Windows
3. Install dependencies
pip install django
4. Run migrations
python manage.py makemigrations
python manage.py migrate
5. Create admin user
python manage.py createsuperuser
6. Run server
python manage.py runserver
Login Details (for testing)
Use the superuser account created above
Project Structure
tracker/ → Main app
templates/ → HTML templates
models.py → Database models
views.py → Application logic
forms.py → Form handling and validation
Author

Felix Omondi


---

# 🚀 AFTER YOU ADD THIS

Run:

```bash
git add README.md
git commit -m "Add project README"
git push