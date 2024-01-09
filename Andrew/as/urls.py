from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Base/', views.Base, name="Base"),
    path('about/', views.about, name="About"),
    path('Dashboard/', views.Dashboard, name="Dashboard"),
    path('Registration/', views.Registration, name="Registration"),
    path('Login/', views.Login, name="Login"),
    path('Contact/', views.Contact, name="Contact"),
    path('shs/', views.shs, name="shs"),
    path('college/', views.college, name="college"),
    path('basiced/', views.basiced, name="basiced"),


]

