from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets, name="pets"),
    path('pet/<int:pet_id>', views.pet, name="pet"),
    path('calender/', views.calender, name="calender")
]