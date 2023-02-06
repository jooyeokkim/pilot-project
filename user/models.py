from django.db import models


class User(models.Model):
    email = models.EmailField('EMAIL', blank=False, null=False, unique=True)
    name = models.CharField('NAME', max_length=50, blank=False, null=False)
    password = models.CharField('PASSWORD', max_length=100)
    is_admin = models.BooleanField('IS_ADMIN', default=False)

    def __str__(self):
        return self.email


class EmailHistory(models.Model):
    email = models.EmailField('EMAIL', blank=False, null=False, unique=True)

    def __str__(self):
        return self.email