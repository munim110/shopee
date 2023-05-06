from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('', home, name='home'),
]