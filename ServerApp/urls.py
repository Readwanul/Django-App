from django.urls import path
from . import views

urlpatterns = [
    path('page2/', views.page2),
    path('page3/', views.page3),
    path('page4/', views.page4),
    path('home/', views.home)
]