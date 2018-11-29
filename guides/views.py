from django.shortcuts import render
from .models import Guide


# Create your views here.

def guides(request):
    guides = Guide.objects.all()
    return render(request, 'guides/guides.html', {'guides': guides})
