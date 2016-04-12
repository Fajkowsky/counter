from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Counter(models.Model):
    word = models.ForeignKey(Word)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
