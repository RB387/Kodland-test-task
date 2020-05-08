from .views import *
from django.urls import path

urlpatterns = [
    path('', home_page, name='home'),
    path('add/', add_post, name='add_post')
]