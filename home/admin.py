from django.contrib import admin
from .models import Contact,user_token
# Register your models here.
admin.site.register(Contact)
admin.site.register(user_token)
