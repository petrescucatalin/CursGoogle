from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    # Include any other fields for the location as necessary

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()
