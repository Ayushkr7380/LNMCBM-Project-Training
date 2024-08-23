
from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test,name='test'),
    path('laptop/',views.laptop,name='laptop'),
    path('fan',views.fan,name='fan'),

    #HW 
    path('abhijeet',views.abhijeet,name='Abhijeet'),
    path('sonu',views.sonu,name='Sonu'),
    path('lucky',views.lucky,name='Lucky'),
    path('aditya',views.aditya,name='Aditya'),
    path('adarsh',views.adarsh,name='Adarsh'),
    path('priyanshu',views.priyanshu,name='Priyanshu'),
    path('ashish',views.ashish,name='Ashish'),
    path('gandhi',views.gandhi,name='Gandhi'),
    path('ashutosh',views.ashutosh,name='Ashutosh'),
    path('suryansh',views.suryansh,name='Suryansh'),
    path('deepak',views.deepak,name='Deepak'),
    path('goldy',views.goldy,name='Goldy'),
    path('shrishty',views.shrishty,name='Shrishty'),
    path('suruchi',views.suruchi,name='Suruchi'),
    path('tanu',views.tanu,name='Tanu'),
    path('sakshi',views.sakshi,name='Sakshi'),
    path('palak',views.palak,name='Palak'),
    path('shilpi',views.shilpi,name='Shilpi'),
    path('aakriti',views.aakriti,name='Aakriti'),
    path('chaitanya',views.chaitanya,name='Chaitanya'),

]
