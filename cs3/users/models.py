# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# New User Model with an exact copy of the default user model.
class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.email