from django.urls import path

from Three import views

urlpatterns = [
    path('index/', views.index)
]