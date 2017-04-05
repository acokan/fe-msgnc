from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    img = models.ImageField(blank=True)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name

