from django.db import models
from django.urls import reverse


class Head(models.Model):
    f1 = models.CharField(max_length=100)
    f2 = models.CharField(max_length=100)

    def __str__(self):
        return self.f1

    def get_absolute_url(self):
        return reverse('head_list')


class Position(models.Model):
    f3 = models.CharField(max_length=100)
    f4 = models.CharField(max_length=100)
    head = models.ForeignKey(Head, on_delete=models.CASCADE)

    def __str__(self):
        return self.f3

    def get_absolute_url(self):
        return reverse('position_list')