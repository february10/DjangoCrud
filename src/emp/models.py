from django.db import models

# Create your models here.


class CRUD (models.Model):
    name = models.CharField(max_length=20,)
    age = models.IntegerField()
    address = models.CharField(max_length=200,)
    department = models.CharField(max_length=30,)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return str(self.name)
