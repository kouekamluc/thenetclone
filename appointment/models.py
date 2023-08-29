from django.db import models
from hospital.models import Mentor 
from django.utils import timezone


# Create your models here.


class Appointment(models.Model):
    time_choices = (
        ('morning','Morning'),
        ('evening','Evening')
    )
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    email = models.EmailField()
    mentor = models.ForeignKey(Mentor , on_delete=models.CASCADE , related_name='appointments')
    date = models.DateField(default=timezone.now)
    time = models.CharField(choices=time_choices , max_length=10)
    note = models.TextField(blank=True , null=True)
    
    def __str__(self):
        return f"{self.name}-{self.mentor.name}"
    