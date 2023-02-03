from django.db import models
from matplotlib.image import thumbnail
from django.urls import reverse

COLOR_CHOICES = (
    ('you-will-love-to-know','You will love to know'),
    ('superhero', 'SuperHero'),
    ('hollywood','Hollywood'),
    ('bollywood','Bollywood'),
    ('anime','Anime'),
)

class playlist(models.Model):
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=300,default="")
    preContent = models.TextField()
    playlist = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="shop/playlistImages", default="")
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    PostViews = models.TextField()
    # Playlist = models.ManyToManyField(playlist)
    PlaylistName = models.CharField(max_length=300,default="none")
    
    category = models.CharField(max_length=60, choices=COLOR_CHOICES, default='you_will_love_to_know')
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
    
    def get_absolute_url(self):
        # return reverse('blogHome',args=[str(self.slug)])
        return f'/blog/{self.slug}'

class User_IP(models.Model):
    userIP=models.TextField(default=None)
    slug = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.userIP + ' - ' + self.slug