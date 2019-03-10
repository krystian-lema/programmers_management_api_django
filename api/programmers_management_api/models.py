from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=40, null=False)

class Paradigm(models.Model):
    name = models.CharField(max_length=20, null=False)

class Language(models.Model):
    name = models.CharField(max_length=40, null=False)
    paradigms = models.ManyToManyField(Paradigm, blank=True)

class Programmer(models.Model):
    firstname = models.CharField(max_length=40, null=False)
    lastname = models.CharField(max_length=40, null=False)
    team = models.ForeignKey(Team, related_name='programmers', on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language, blank=True)

