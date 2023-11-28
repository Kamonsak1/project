from django.shortcuts import render
from myweb.models import *
# Create your views here.
def home(req):
    c = course.objects.all()
    return render(req,'main/home.html',{'c':c})
