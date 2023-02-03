from django.db import models
from matplotlib.image import thumbnail
from django.urls import reverse

COLOR_CHOICES = (
    ('cricket','cricket'),
)


class Cricketpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    PostViews = models.TextField()
    category = models.CharField(max_length=60, choices=COLOR_CHOICES, default='cricket')
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    preContent = models.TextField()
    content = models.TextField()
    slug = models.CharField(max_length=500, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="shop/images", default="")
    poster = models.ImageField(upload_to="shop/images", default="")
    tag = models.TextField(default="post")

    def __str__(self):
        return self.title + ' by ' + self.author
        
class User_IP(models.Model):
    userIP=models.TextField(default=None)
    slug = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.userIP + ' - ' + self.slug