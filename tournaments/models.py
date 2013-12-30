from django.db import models
from pinMachines.models import *
from player.models import *
from scores.models import *
from datetime import datetime
# Create your models here.


class Tournament( models.Model ):
    name = models.CharField( max_length = 300 )
    location = models.ForeignKey( 'pinMachines.Location' )
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __unicode__(self):
        return self.name

class Match( models.Model ):
    tournament = models.ForeignKey( Tournament )
    machine = models.ForeignKey( 'pinMachines.Machine' )
    player = models.ForeignKey( 'player.Player' )
    outcome = models.CharField( max_length = 2 )
    score = models.ForeignKey( 'scores.TourneyScore' )
    
    def __unicode__(self):
        return self.name

class Results( models.Model ):
    tournament = models.ForeignKey( Tournament )
    player = models.ForeignKey( 'player.Player' )
    outcome = models.CharField( max_length = 4 )
    
    def __unicode__(self):
        return self.name