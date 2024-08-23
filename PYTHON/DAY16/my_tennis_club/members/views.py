from .forms import MemberForm,StudentForm
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members(request):
    context = {}
    #create object of form
    form = MemberForm(request.POST or None,request.FILES or None)
    #check if the form data is valid
    if form.is_valid():
        #save the form data to model
        form.save()
    context['form']=form
    return render(request,'myfirst.html',context)

def add_students(request):
    context={}
    form = StudentForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request,'stu.html',context)