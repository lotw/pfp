from django.db import models
from pinMachines.models import *
from player.models import *
# Create your models here.


class HighScore( models.Model ):
    player = models.ForeignKey( 'player.Player' )
    machine = models.ForeignKey( 'pinMachines.Machine' )
    score = models.CharField( max_length = 55 )

    def __unicode__(self):
        return self.name

class TourneyScore( models.Model ):
    player = models.ForeignKey( 'player.Player' )
    machine = models.ForeignKey( 'pinMachines.Machine' )
    score = models.CharField( max_length = 55 )

    def __unicode__(self):
        return self.name

