from django.db import models

# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    yearMfd = models.CharField(max_length=4)
    
    def __unicode__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phoneNum = models.CharField(max_length=20)
        
    def __unicode__(self):
        return self.name

class OnLocation(models.Model):
    location = models.ForeignKey(Machine)
    machine = models.ForeignKey(Location)
    dateIn = models.DateTimeField()

class Repair(models.Model):
    machine = models.ForeignKey(Location)
    location = models.ForeignKey(Machine)
    dateAdded = models.DateTimeField()
    dateRepaired = models.DateTimeField()
    problemNotes = models.CharField(max_length=800)
    repairNotes = models.CharField(max_length=800)
    #assignedTo = models.ForeignKey(PinTech)
