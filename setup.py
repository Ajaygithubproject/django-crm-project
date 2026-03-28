#!/usr/bin/env python
"""
Run this once to set up the database and create the admin user.
Usage:  python setup.py
"""
import os, sys, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'immigratecrm.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

print("📦 Running migrations...")
call_command('makemigrations', 'crm', verbosity=0)
call_command('migrate', verbosity=0)

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@immigratecrm.com', 'admin')
    print("✅ Admin user created  →  username: admin  |  password: admin")
else:
    print("ℹ️  Admin user already exists.")

print("\n🚀 Setup complete! Run the server:")
print("   python manage.py runserver")
print("\n🌐 Open:  http://127.0.0.1:8000")
print("🔑 Login: admin / admin\n")
