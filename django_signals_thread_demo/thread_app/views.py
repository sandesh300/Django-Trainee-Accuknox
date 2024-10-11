from django.http import HttpResponse
from .models import ThreadModel
import threading

def create_thread_model(request):
    current_thread = threading.current_thread()
    print(f"View function thread: {current_thread.name}")
    
    obj = ThreadModel.objects.create(name="Thread Test Object")
    
    return HttpResponse("ThreadModel object created. Check console for thread information.")