from django.urls import path,include
from myweb.views import *
urlpatterns = [
    path("", home,name='home'),

]