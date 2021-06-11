from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path('login',views.loginuser, name="login"),
    path('logout',views.logoutuser, name="logout"),
    path('data1',views.datauser1, name="data1"),
    path('data2',views.datauser2, name="data2"),
    path('data3',views.datauser3, name="data3"),
    path('data4',views.datauser4, name="data4"),
    path('prog1',views.proguser1, name="prog1"),
    path('prog2',views.proguser2, name="prog2"),
    path('prog3',views.proguser3, name="prog3"),
    path('prog4',views.proguser4, name="prog4"),
    path('select',views.selectuser, name="select"),
    path('knn_graph',views.knn_graphuser, name="knn_graph"),
    path('rand_graph',views.rand_graphuser, name="rand_graph"),
    path('about',views.aboutuser, name="about"),
    path('work',views.workuser, name="work"),
    path('price',views.priceuser, name="price"),
    path('contact',views.contactuser, name="contact"),
    path('index',views.indexuser, name="index"),


]