from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #first_name = models.CharField('user.get_first_name', max_length=50)
    #courses = models.ManyToManyField(Course)
    # add more stuff

    def __str__(self):
        return f'Olá {self.user.get_full_name}!'