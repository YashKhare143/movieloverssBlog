from django.urls import path
from blog import views
from django.conf.urls.static import static

urlpatterns = [
    path("",views.blogHome, name="blogHome"),
    path("<str:slug>",views.blogpost, name="blogPost"),
    path("category/you-will-love-to-know",views.category_youWillLoveToKnow, name="category"),
    path("category/superhero",views.category_superhero, name="category"),
    path("category/hollywood",views.category_hollywood, name="category"),
    path("category/bollywood",views.category_bollywood, name="category"),
    path("category/anime",views.category_anime, name="category"),

]
