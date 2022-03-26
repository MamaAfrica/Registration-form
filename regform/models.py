from django.db import models


GENDER_CHOICES = [('Male','Male'), ('Female','Female')]
EVENT_CHOICES = [('Perform','Perform'), ('Dynatrace go','Dynatrace go'), ('Amplify','Amplify')]


class Register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    event = models.CharField(max_length=20, choices=EVENT_CHOICES, null=True)
    event_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.last_name

