from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=200)


class Counter(models.Model):
    word = models.ForeignKey(Word)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
