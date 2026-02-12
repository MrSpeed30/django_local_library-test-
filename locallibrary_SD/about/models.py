from django.db import models

# Create your models here.

#review tab's data where user inputs his thoughts
class review(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    date = models.TimeField(auto_now=True)
    comment = models.TextField(max_length=1500)