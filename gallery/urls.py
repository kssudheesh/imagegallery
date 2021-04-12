from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name='index'),
    path('show/<str:pk>/', views.show, name='show')
]
