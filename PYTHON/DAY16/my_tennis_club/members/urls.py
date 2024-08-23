from django.urls import path
from . import views

urlpatterns= [
    path('members/',views.members,name='members'),
    path('add_students/',views.add_students,name='add_students'),
]