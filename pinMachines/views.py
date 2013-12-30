from django.shortcuts import render
from django.http import HttpResponse
from pinMachines.models import *
import json
from datetime import datetime

def ajaxAddMachine(request):
    
    # init variables needed for adding the machine
    name = ''
    mfu = ''
    year = ''

    response = ''

    # grab the variables from the request
    if request.GET.has_key('name') and request.GET['name'] != '':
        name = request.GET['name']

    if request.GET.has_key('mfu') and request.GET['mfu'] != '':
        mfu = request.GET['mfu']

    if request.GET.has_key('year') and request.GET['year'] != '':
        year = request.GET['year']

    # create a new Machine
    try:
        # Add the machine
        mach = Machine(name = name, manufacturer = mfu, yearMfd = year)
        mach.save()

        # auto assign it to the unassigned location
        
        # grab the unassigned location
        location = Location.objects.get(id = 1)
        assign = OnLocation(location = location, machine = mach)
        assign.save()
        
        response = 'Success'
    except:
        response = 'ERRORORREORRROERROR'

    return HttpResponse( json.dumps(response), mimetype="application/json")

def ajaxAddLocation(request):
    
    # init variables
    name = ''
    address = ''
    phone = ''

    response = ''

    # grab the variables from the request
    if request.GET.has_key('name') and request.GET['name'] != '':
        name = request.GET['name']

    if request.GET.has_key('addr') and request.GET['addr'] != '':
        address = request.GET['addr']

    if request.GET.has_key('phone') and request.GET['phone'] != '':
        phone = request.GET['phone']

    # create a new Location
    try:
        loc = Location(name = name, address = address, phoneNum = phone)
        loc.save()
        response = 'Success'
    except:
        response = 'ERRORORREORRROERROR'


    return HttpResponse( json.dumps(response), mimetype="application/json")

def ajaxAssignMachine(request):
    
    # init variables
    location = ''
    machine = ''
    machines = []
    response = ''

    # grab the variables from the request
    if request.GET.has_key('locID') and request.GET['locID'] != '':
        location = Location.objects.get(id = request.GET['locID'])

    if request.GET.has_key('machines[]') and len(request.GET.getlist('machines[]')) != 0:
        machines = request.GET.getlist('machines[]')

    # assign the games to the location   
    for machID in machines:
        machine = Machine.objects.get( id = machID)
        try:
            # if it fails then it already exists and needs to be updated not created Could probably clean this up a good deal
            try:
                assign = OnLocation(location = location, machine = machine)
                assign.save()
            except:
                # this means its already onlocation even if just unassigned
                update = OnLocation.objects.get( machine = machine )
                update.location = location
                update.save()
            response = 'Success'
        except:
            response = 'ERRORORREORRROERROR'


    return HttpResponse( json.dumps(response), mimetype="application/json")