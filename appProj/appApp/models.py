from django.db import models

# Create your models here.

# model for application
class Application(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    pNum = models.IntegerField()

# to display name in admin site
    def __str__(self):
        return self.fName
