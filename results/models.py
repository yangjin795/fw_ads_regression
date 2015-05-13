from django.db import models
from django.contrib.auth.models import User
import cases.models
# Create your models here.


class TestResult(models.Model):
    name = models.CharField(max_length=20,null=True)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    user_run = models.ForeignKey(User)
    ads_revision = models.CharField(max_length=20)

class CaseResult(models.Model):
    result = models.ForeignKey(TestResult)
    case = models.ForeignKey(cases.models.TestCase)
    FAILED='F'
    PASSED='P'
    WARNING='W'
    case_result = models.CharField(max_length=20,choices=((FAILED,'Failed'),(PASSED,'Pass'),(WARNING,'Warning')))

