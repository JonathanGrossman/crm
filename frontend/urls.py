from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('students/', views.index),
    path('add-student/', views.index),
    path('edit-student/:id', views.index)
]