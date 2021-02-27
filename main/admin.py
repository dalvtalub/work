# Adding a table to the admin panel

from django.contrib import admin
from .models import Matches, Articles, Teams, Cards

admin.site.register(Matches)
admin.site.register(Articles)
admin.site.register(Teams)
admin.site.register(Cards)
# After you need to register in the terminal: python manage.py makemigrations
# and python manage.py migrate
