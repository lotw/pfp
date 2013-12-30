from django.shortcuts import render
from django.http import HttpResponse
from pinMachines.models import *
import json

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
        mach = Machine(name = name, manufacturer = mfu, yearMfd = year)
        mach.save()
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
    locID = ''
    machines = list

    response = ''

    # grab the variables from the request
    if request.GET.has_key('locID') and request.GET['locID'] != '':
        locID = request.GET['locID']

    if request.GET.has_key('machines') and request.GET['machines'] != '':
        machines = request.GET['machines']

    # assign the games to the location
    try:
        loc = Location(name = name, address = address, phoneNum = phone)
        loc.save()
        response = 'Success'
    except:
        response = 'ERRORORREORRROERROR'


    return HttpResponse( json.dumps(response), mimetype="application/json")