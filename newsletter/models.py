from django.db import models


class Signup(models.Model):
    email = models.EmailField()
    confirmationId = models.IntegerField()
    confirmed = models.BooleanField()
