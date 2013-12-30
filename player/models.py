from django.db import models

# Create your models here.


class Player( models.Model ):
    name = models.CharField( max_length = 300 )
    initials = models.CharField( max_length = 3 )
    phone = models.CharField( max_length = 15 )
    email = models.CharField( max_length = 55 )

    def __unicode__(self):
        return self.name
