from __future__ import unicode_literals
from django.db import models

class Coursemanager(models.Manager):
    def addcourse(self, postdata):
        if postdata:
            self.create(name=postdata['name'],description=postdata['description'])

    def removecourse(self, postdata):
        if postdata:
            Course.objects.filter(id=postdata).delete()

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Coursemanager()
