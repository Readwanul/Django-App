from django.urls import path
from . import views

urlpatterns = [
    path('page2/', views.page2),
    path('page3/', views.page3,name='page3'),
    path('page4/', views.page4,name='page4'),
    path('add_student/', views.add_student,name='add_student'),
    path('delete_student/<int:student_id>/', views.delete_student,name='delete_student'),
    path('home/', views.home)
]