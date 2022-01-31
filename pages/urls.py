from django.urls import path 
from .views import HomePgaeView 

urlpatterns = [
    path('',HomePgaeView.as_view(),name="home"),
]