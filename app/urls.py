from django.urls import path, include
from .views import Home, KeyInput, ClubChartView

urlpatterns = [

    path('', Home, name='home'),
    path('keyin/', KeyInput, name='keyin'),
    path('chart/', ClubChartView.as_view(), name='chart'),
]
