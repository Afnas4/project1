from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.home,name='home'),
    path('course',views.course,name="course"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('contact',views.contact,name="contact"),
    path('aboutus',views.contact,name="aboutus"),
    path('gallery',views.gallery,name="gallery"),
    path('forgot',views.forgot,name="forgot"),
    
]

