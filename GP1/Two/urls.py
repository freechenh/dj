# from django.conf.urls import url
from django.urls import path

from Two import views

urlpatterns = [
    path('index/', views.index),
    path('addStudent/', views.add_student),
    path('getStudents/', views.get_students),
    path('updateStudent/', views.update_student),
    path('deleteStudent/', views.delete_student),
]
