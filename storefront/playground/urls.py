from django.urls import path 
from . import views 

# A URLConf module
urlpatterns = [
    path('hello/', views.say_hello)
] 