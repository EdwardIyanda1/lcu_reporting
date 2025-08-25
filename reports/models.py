from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('Harassment', 'Harassment'),
        ('Discrimination', 'Discrimination'),
        ('Safety Concern', 'Safety Concern'),
    ]
    
    full_name = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    date_of_incident = models.DateField()
    contact_info = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Report #{self.id} - {self.category}"