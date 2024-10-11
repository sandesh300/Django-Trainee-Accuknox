
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal handler started for {instance.name}")
    time.sleep(5)  # Simulate some time-consuming task
    print(f"Signal handler finished for {instance.name}")