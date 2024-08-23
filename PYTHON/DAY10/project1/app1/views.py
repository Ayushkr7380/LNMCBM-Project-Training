from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def view_pink(request):
    temp = loader.get_template('pink.html')
    return HttpResponse(temp.render())

def view_blue(request):
    temp = loader.get_template('blue.html')
    return HttpResponse(temp.render())

def view_darkSalmon(request):
    temp = loader.get_template('darksalmon.html')
    return HttpResponse(temp.render())

def test(request):
    return HttpResponse('<h1>Ayush</h1>')

def laptop(request):
    return HttpResponse('<h1>This laptop is working..</h1>')

def fan(request):
    return HttpResponse('<h1>This fan is very fast..</h1>')

# HW to create 20 functions 

def view_aliceblue(request):
    temp = loader.get_template('aliceblue.html')
    return HttpResponse(temp.render())

def view_antiquewhite(request):
    temp = loader.get_template('antiquewhite.html')
    return HttpResponse(temp.render())

def view_black(request):
    temp = loader.get_template('black.html')
    return HttpResponse(temp.render())


def view_blueviolet(request):
    temp = loader.get_template('blueviolet.html')
    return HttpResponse(temp.render())

def view_brown(request):
    temp = loader.get_template('brown.html')
    return HttpResponse(temp.render())

def view_burlywood(request):
    temp = loader.get_template('burlywood.html')
    return HttpResponse(temp.render())

def view_cadetblue(request):
    temp = loader.get_template('cadetblue.html')
    return HttpResponse(temp.render())

def view_coral(request):
    temp = loader.get_template('coral.html')
    return HttpResponse(temp.render())

def view_cornflowerblue(request):
    temp = loader.get_template('cornflowerblue.html')
    return HttpResponse(temp.render())

def view_cornsilk(request):
    temp = loader.get_template('cornsilk.html')
    return HttpResponse(temp.render())

def view_crimson(request):
    temp = loader.get_template('crimson.html')
    return HttpResponse(temp.render())

def view_cyan(request):
    temp = loader.get_template('cyan.html')
    return HttpResponse(temp.render())

def view_darkblue(request):
    temp = loader.get_template('darkblue.html')
    return HttpResponse(temp.render())

def view_darkcyan(request):
    temp = loader.get_template('darkcyan.html')
    return HttpResponse(temp.render())

def view_darkgoldenrod(request):
    temp = loader.get_template('darkgoldenrod.html')
    return HttpResponse(temp.render())

def view_darkgray(request):
    temp = loader.get_template('darkgray.html')
    return HttpResponse(temp.render())

def view_darkgreen(request):
    temp = loader.get_template('darkgreen.html')
    return HttpResponse(temp.render())

def view_darkred(request):
    temp = loader.get_template('darkred.html')
    return HttpResponse(temp.render())

def view_deeppink(request):
    temp = loader.get_template('deeppink.html')
    return HttpResponse(temp.render())

def view_dimgrey(request):
    temp = loader.get_template('dimgrey.html')
    return HttpResponse(temp.render())
