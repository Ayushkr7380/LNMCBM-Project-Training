from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse('<h1>BCA section D is learning django again</h1>')