from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Applicant(AbstractUser):
    is_penn_student = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.is_penn_student = self.email.endswith('@upenn.edu') or self.email.endswith('@sas.upenn.edu') or self.email.endswith('@seas.upenn.edu') or self.email.endswith('@wharton.upenn.edu') or self.email.endswith('@nursing.upenn.edu')
        super().save(*args, **kwargs)

class Application(models.Model):
    STATUS_CHOICES = [
        ("ACPT", "Accepted"),
        ("RJCT", "Rejected"),
        ("WLST", "Waitlisted"),
        ("PROC", "Processing"),
    ]
    YEAR_CHOICES = [
        ("nth","Ninth Grade"), ("ten","Tenth Grade"), ("ele","Eleventh Grade"), ("twl","Twelfth Grade"), ("fr","Freshman"), ("so","Sophomore"), ("ju","Junior"), ("se","Senior"), ("gr","Grad")
    ]
    HACKATHON_CHOICES = [
        ("y","Yes"), ("n","No")
    ]
    applicant = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="PROC")
    school = models.CharField(max_length=100,default="")
    year = models.CharField(max_length=3, choices=YEAR_CHOICES, default="nth")
    major = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=12, default='123-456-7890')
    birthday = models.DateField(default="2000-01-01")
    q1 = models.TextField(default="")
    q2 = models.TextField(default="")
    first_hackathon = models.CharField(max_length=1,default="b",choices=HACKATHON_CHOICES)
    team_member_1 = models.EmailField(max_length=100, blank=True, default='',null=True)
    team_member_2 = models.EmailField(max_length=100, blank=True, default='',null=True)
    team_member_3 = models.EmailField(max_length=100, blank=True, default='',null=True)