from django.urls import path, include
from .views import *

urlpatterns = [

    path('', Home, name='home'),
    path('keyin/', KeyInput, name='keyin'),
    path('chart/', Chart, name='chart',)
]
