from django.contrib.sitemaps import Sitemap
from .models import Blogpost
from django.urls import reverse

class HomeSitemap(Sitemap):
    def items(self):
        return ['home','blogHome','aboutus','contactus']
        
    def location(self,item):
        return reverse(item)

class PostSitemap(Sitemap):
    def items(self):
        return Blogpost.objects.all()
        
