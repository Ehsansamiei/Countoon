# 🧮 Bestoon - Accounting System

A lightweight Django-based accounting web app where each user can register, log in, and manage their own expenses and incomes securely.

## 🚀 Features
- User registration & login system with CAPTCHA
- User-specific dashboards
- Expense & income tracking
- Admin panel for data management

## 🧠 Tech Stack
- Python 3.12
- Django 5.x
- Bootstrap 5
- SQLite / PostgreSQL (configurable)

## ⚙️ Installation
```bash
git clone https://github.com/YourUsername/YourRepo.git
cd YourRepo
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
