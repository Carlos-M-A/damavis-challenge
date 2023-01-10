from django.urls import path, include
from rest_framework import routers
from . import views



urlpatterns = [

    path('dispenser/', views.DispenserCreate.as_view()),
    path('dispenser/<uuid:unique_id>/status', views.DispenserUpdate.as_view()),
    path('dispenser/<uuid:unique_id>/spending', views.DisperserRetrieve.as_view()),



]