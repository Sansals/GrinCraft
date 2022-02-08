from django.urls import path, include
from .views import *

urlpatterns = [
    path('', redirect_user, name='redirect'),
    path('signup/', create_user, name='signup'),
    path('auth1/', send_code, name = 'send_code'),
    path('confirm/', confirmation_user, name='confirmation_user'),
    path('login/', login_user, name='login'),
    path('logout/', logout_func, name='logout'),
    path('welcome/', signup_complete, name='welcome'),
    path('emailadd/', emailadd, name='emailadd')
]