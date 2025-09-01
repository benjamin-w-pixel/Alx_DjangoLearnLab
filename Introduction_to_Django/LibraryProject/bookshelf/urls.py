from django.urls import path
from . import views

urlpatterns = [
path ('bookshelf/',views.say_hello)     
]