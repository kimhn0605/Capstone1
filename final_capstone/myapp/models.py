from django.db import models

class ShootingLocation(models.Model) :
  position = models.TextField(blank=True, null=True)