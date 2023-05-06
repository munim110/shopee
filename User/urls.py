from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('user_profile/', user_profile, name='user_profile'),
    path('', home, name='home'),
]