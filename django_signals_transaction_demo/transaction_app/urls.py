from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_parent_and_child, name='create_parent_and_child'),
]