from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from pinMachines.models import *

""" The PFP homepage """
def homepage(request):

    return render(request, 'home.html')


def machinesPage(request):

    machines = Machine.objects.all()
    locations = Location.objects.all()
    
    return render(
        request, 
        'machines.html',
        {
            'machines': machines,
            'locations': locations
        }
    )

def tournamentsPage(request):
    
    # grab all the locations to send to the tournament page
    locations = Location.objects.all()

    return render(
        request,
        'tournaments.html',
        {
            'locations': locations
        }
    )