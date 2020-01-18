from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contactNumber = models.CharField(max_length=13)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email
