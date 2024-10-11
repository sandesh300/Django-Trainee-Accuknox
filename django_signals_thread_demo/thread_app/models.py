from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time

class ThreadModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=ThreadModel)
def thread_signal_handler(sender, instance, created, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal handler started for {instance.name}")
    print(f"Signal handler thread: {current_thread.name}")
    time.sleep(2)  # Simulate some time-consuming task
    print(f"Signal handler finished for {instance.name}")