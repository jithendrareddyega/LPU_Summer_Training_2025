from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=20)
    diagnosis = models.TextField()
    admission_date = models.DateField()

    def __str__(self):
        return self.name
