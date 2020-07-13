from django.urls import path, include
from .views import Home, KeyInput

urlpatterns = [

    path('', Home, name='home'),
    path('keyin/', KeyInput, name='keyin'),

]
