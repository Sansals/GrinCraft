from django.urls import path, include
from .views import *

urlpatterns = [
    path('', profile_page, name='profile'),
    path('info/', profile_info_page, name='profile-info')
]