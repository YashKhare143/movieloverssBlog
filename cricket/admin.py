from django.contrib import admin

from cricket.models import Cricketpost,User_IP
# Register your models here.
admin.site.register(User_IP)
@admin.register(Cricketpost)
class CricketpostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
    