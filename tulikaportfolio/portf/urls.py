from django.urls import path
from portf import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
]