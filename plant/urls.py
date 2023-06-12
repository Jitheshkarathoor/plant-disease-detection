from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',LoginView.as_view(template_name='login.html'),name="login"),
    path('afterlogin',views.afterlogin_view,name='afterlogin'),
    path('home/',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('upload/',views.upload,name="upload"),
    path('upload1/',views.upload1,name="upload1"),
    path('tomato/',views.tomato,name="tomato"),
    path('predict/',views.predict,name="predict"),
    path('predict1/',views.predict1,name="predict1"),
    path('result/',views.result,name="result"),
    path('chilli/',views.chilli,name="chilli"),
    path('rice/',views.rice,name="rice"),
    path('corn/',views.corn,name="corn"),


]