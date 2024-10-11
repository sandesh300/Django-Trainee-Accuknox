from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class Parent(models.Model):
    name = models.CharField(max_length=100)

class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

@receiver(post_save, sender=Parent)
def create_child(sender, instance, created, **kwargs):
    if created:
        Child.objects.create(parent=instance, name=f"Child of {instance.name}")
        print(f"Child created for {instance.name}")
        raise Exception("Simulated error in signal handler")