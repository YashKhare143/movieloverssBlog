from django.contrib import admin

from blog.models import Blogpost,User_IP,playlist
# Register your models here.
admin.site.register(User_IP)
admin.site.register(playlist)
@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
    