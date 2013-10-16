from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s %s: %s' % (self.first_name, self.last_name, self.age)
