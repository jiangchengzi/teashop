from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from login.models import Users
# Create your views here.

def Login(request):
    s=Users.objects.all()
    t=loader.get_template('login.html')
    c=Context({'shop':s})
    return HttpResponse(t.render(c))
