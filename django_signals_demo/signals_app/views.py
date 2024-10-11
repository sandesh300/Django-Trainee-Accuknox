from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import MyModel
import time

def create_model(request):
    start_time = time.time()
    
    obj = MyModel.objects.create(name="Test Object")
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return HttpResponse(f"Object created. Total execution time: {execution_time:.2f} seconds")