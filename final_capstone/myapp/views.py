from django.shortcuts import render
from django.http import HttpResponse
from .models import ShootingLocation
# Create your views here.
def home(request) :

  shooting_location = ShootingLocation.objects.all()
  context = {"shooting_location" : shooting_location}
  return render(request, 'home.html', context)

def table(request) :
  result = ''
  result += "안뇽"
  return HttpResponse(result)