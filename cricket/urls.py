from django.urls import path
from cricket import views
from django.conf.urls.static import static

urlpatterns = [
    path("",views.cricketHome, name="cricketHome"),
    path("<str:slug>",views.cricketpost, name="cricketPost"),
    

]
