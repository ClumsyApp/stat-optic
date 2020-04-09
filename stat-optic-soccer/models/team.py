from django.db import models

class Team(models.Model):

    name = models.CharField(db_index=True, max_length=512, unique=False, blank=False, null=True)
    #sport = 
