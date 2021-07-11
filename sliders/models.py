from django.db import models


class Slider(models.Model):

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='slider/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
