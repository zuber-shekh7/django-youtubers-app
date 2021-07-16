from django.db import models


class Team(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255)
    facebook_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='roles/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
