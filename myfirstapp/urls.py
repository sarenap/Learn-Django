from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfunctioncall,name="index"),
    path('about',views.myfunctionabout,name="about"),
    path('add/<int:a>/<int:b>',views.add,name="add"),
    path('intro/<str:name>/<int:age>',views.intro,name="intro"),

    #binary string to decimal website converter.
    path('decToBase/<int:num>/<int:base>', views.decToBase, name="decToBase"),

    path('myfirstpage',views.myfirstpage,name='myfirstpage'),
    path('mysecondpage',views.mysecondpage,name='mysecondpage'),
    path('mythirdpage',views.mythirdpage,name='mythirdpage'),
    path('myimagepage', views.myimagepage, name='myimagepage'), #views. call that function
    path('myimagepage2', views.myimagepage2, name='myimagepage2'),
    path('imagepage3', views.imagepage3, name='imagepage3'),
    path('imagepage4', views.imagepage4, name='imagepage4'),
    path('imagepage5/<str:imagename>', views.imagepage5, name='imagepage5'),
    path('myform', views.myform, name='myform'),
    path('submitmyform', views.submitmyform, name='submitmyform'),
    path('myform2', views.myform2, name='myform2'),
]