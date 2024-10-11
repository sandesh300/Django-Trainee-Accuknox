from django.urls import path
from . import views

urlpatterns = [
    path('create-thread/', views.create_thread_model, name='create_thread_model'),
]