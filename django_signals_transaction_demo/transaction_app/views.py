from django.http import HttpResponse
from .models import Parent, Child
from django.db import transaction

def create_parent_and_child(request):
    try:
        with transaction.atomic():
            parent = Parent.objects.create(name="Test Parent")
            print(f"Parent created: {parent.name}")
            # If signals run outside the transaction, we would see a Parent object
            # created even though the Child creation fails
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return HttpResponse(f"Error occurred: {str(e)}")

    parent_count = Parent.objects.count()
    child_count = Child.objects.count()
    return HttpResponse(f"Parents: {parent_count}, Children: {child_count}")