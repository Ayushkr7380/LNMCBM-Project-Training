from .models import Member
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members(request):
    temp = loader.get_template('myfirst.html')
    x = Member.objects.all()[5]
    context = {
        'firstname' : x.firstname,
    }
    return HttpResponse(temp.render(context,request))
