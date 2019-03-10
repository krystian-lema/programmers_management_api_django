from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=40, null=False)

class Programmer(models.Model):
    firstname = models.CharField(max_length=40, null=False)
    lastname = models.CharField(max_length=40, null=False)
    team = models.ForeignKey(Author, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

class Language(models.Model):
    name = models.CharField(max_length=40, null=False)
    programmers = models.ManyToManyField(Programmer)
    paradigms = models.ManyToManyField(Paradigm)

class Paradigm(models.Model):
    name = models.CharField(max_length=20, null=False)
    languages = models.ManyToManyField(Language)
