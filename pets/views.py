from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet, Appointment


def home(request):
    return render(request, 'home.html')

def pets(request):
  context = {
    'pets': Pet.objects.filter()
  }
  return render(request, 'pets.html', context)

def pet(request, pet_id):
    context = {
    'pet': Pet.objects.get(id=pet_id),
    'appointments' : Appointment.objects.all()
    }
    return render(request, 'pet.html', context)

def calender(request):
  context = {
    'appointments': Appointment.objects.order_by('date_of_appointment')
  }
  return render(request, 'calender.html', context)