# 🧮 Countoon - Accounting System

A lightweight Django-based accounting web app where each user can register, log in, and manage their own expenses and incomes securely.
---

- webapp address : https://drakestoon.ir
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
git clone https://github.com/Ehsansamiei/bestoon.git
cd bestoon
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔑 Environment Variables
- Create a .env file with your keys:

```bash
RECAPTCHA_PUBLIC_KEY=your_key_here
RECAPTCHA_PRIVATE_KEY=your_key_here
```

## 👤 Developer

- Drake 💻Backend Developer
- 📫 Contact: ehsan.samiei84@gmail.com