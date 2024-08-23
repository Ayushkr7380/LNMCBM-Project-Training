from django import forms 
from .models import Member,Student

class MemberForm(forms.ModelForm):
    #Specify the name of model to use..
    class Meta:
        model = Member
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'