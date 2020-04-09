from django.db import models

class Player(models.Model):

    first_name = models.CharField(db_index=True, max_length=512, unique=False, blank=False, null=True)
    last_name = models.CharField(db_index=True, max_length=512, unique=False, blank=True, null=True)
    number = models.PositiveIntegerField(db_index=True)
    #team = 
