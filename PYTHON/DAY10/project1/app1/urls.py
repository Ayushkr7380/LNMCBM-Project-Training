
from django.urls import path
from . import views

urlpatterns = [
    path('view_pink/',views.view_pink,name='view_pink'),

    path('view_blue/',views.view_blue,name='view_blue'),

    path('view_darkSalmon/',views.view_darkSalmon,name='view_darkSalmon'),

    path('test/',views.test,name='test'),
    path('laptop/',views.laptop,name='laptop'),
    path('fan/',views.fan,name='fan'),

    #HW 

     path('view_aliceblue/',views.view_aliceblue,name='view_aliceblue'),

     path('view_antiquewhite/',views.view_antiquewhite,name='view_antiquewhite'),

     path('view_black/',views.view_black,name='view_black'),

     path('view_blueviolet/',views.view_blueviolet,name='view_blueviolet'),

     path('view_brown/',views.view_brown,name='view_brown'),

     path('view_burlywood/',views.view_burlywood,name='view_burlywood'),

     path('view_cadetblue/',views.view_cadetblue,name='view_cadetblue'),

     path('view_coral/',views.view_coral,name='view_coral'),

     path('view_cornflowerblue/',views.view_cornflowerblue,name='view_cornflowerblue'),

     path('view_cornsilk/',views.view_cornsilk,name='view_cornsilk'),

     path('view_crimson/',views.view_crimson,name='view_crimson'),

     path('view_cyan/',views.view_cyan,name='view_cyan'),

     path('view_darkblue/',views.view_darkblue,name='view_darkblue'),

     path('view_darkcyan/',views.view_darkcyan,name='view_darkcyan'),

     path('view_darkgoldenrod/',views.view_darkgoldenrod,name='view_darkgoldenrod'),

     path('view_darkgray/',views.view_darkgray,name='view_darkgray'),

     path('view_darkgreen/',views.view_darkgreen,name='view_darkgreen'),

     path('view_darkred/',views.view_darkred,name='view_darkred'),

     path('view_deeppink/',views.view_deeppink,name='view_deeppink'),

     path('view_dimgrey/',views.view_dimgrey,name='view_dimgrey'),

     
   

]
