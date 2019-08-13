import csv, sys, os, django

proj_path = "/home/vaibhav/MSP-Recruitment-Web-Portal/"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_portal.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth import authenticate
from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.conf import settings
User = get_user_model()

file = 'passwords.csv'

data = csv.reader(open(file), delimiter=",")
for row in data:
    if row[0] != "Number":
    # Post.id = row[0]
        Post=User()
        Post.password = make_password(row[1])
        Post.username = row[0]
        Post.email = ''
        Post.save()