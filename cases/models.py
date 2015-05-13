from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CaseGroup(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User)


class TestCase(models.Model):
    name=models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User,related_name="creator")
    owner = models.ForeignKey(User,related_name="owner")
    description = models.TextField()

class CaseData(models.Model):
    case = models.ForeignKey(TestCase)
    base_sql = models.CharField(max_length=50)
    case_sql = models.CharField(max_length=50)

class CaseRequest(models.Model):
    case = models.ForeignKey(TestCase)
    file_name = models.CharField(max_length=50)
    TYPE_C='c'
    TYPE_B='b'
    type = models.CharField(max_length=20,choices=((TYPE_C,'typeC'),(TYPE_B,'typeB')))
    description = models.TextField()
    sequence = models.IntegerField()
    class Meta:
        unique_together