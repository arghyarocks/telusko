from django.shortcuts import render
from django.http import HttpResponse
from .models import Destinations
# Create your views here.
def index(request):
    dest1 = Destinations()
    dest1.name="Mumbai"
    dest1.desc="The city that never sleeps"
    dest1.price= 700
    dest1.img ='destination_1.jpg'

    dest2 = Destinations()
    dest2.name="kolkata"
    dest2.desc="city of joy"
    dest2.price= 676
    dest2.img ='destination_2.jpg'

    dest3 = Destinations()
    dest3.name="Bangalore"
    dest3.desc="The city of Gardens and offices"
    dest3.price= 787
    dest3.img ='destination_3.jpg'

    dests= [dest1,dest2,dest3]

    return render(request,'index.html' , {'dests': dests})
