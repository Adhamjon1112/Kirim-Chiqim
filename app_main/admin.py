from django.contrib import admin
from django.contrib.auth import get_user_model

from app_main.models import Transaction


User = get_user_model()

admin.site.register(User)
admin.site.register(Transaction)