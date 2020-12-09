from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=200)


class Student(models.Model):
    s_name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    s_id = models.ForeignKey(Grade, on_delete=models.CASCADE)
