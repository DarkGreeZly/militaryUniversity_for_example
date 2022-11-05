from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    details = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.id}: {self.first_name} {self.last_name}, his e-mail: {self.email} and {self.phone}. Details was left: {self.details}'
