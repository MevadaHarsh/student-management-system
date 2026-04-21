from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    enno = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"