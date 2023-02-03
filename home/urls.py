from django.urls import path
from home import views


urlpatterns = [
    path('',views.home, name="home"),
    path('aboutus',views.aboutus, name='aboutus'),
    path('contactus',views.contactus, name='contactus'),
     path('subscribeUs' , views.subscribeUs, name='subscribeUs'),
    path('search',views.search, name='search'),

]
