from django.db import models
from ckeditor.fields import RichTextField


class Youtuber(models.Model):
    # crew choices
    SOLO = 'solo'
    SMALL = 'small'
    LARGE = 'large'

    # camera choices
    CANON = 'canon'
    NIKON = 'nikon'
    SONY = 'sony'
    PANASONIC = 'panasonic'
    FUJI = 'fuji'
    RED = 'red'
    OTHER = 'other'

    # category choices
    CODE = 'code'
    REVIEWS = 'reviews'
    VLOGS = 'vlogs'
    COMEDY = 'comedy'
    GAMING = 'gaming'
    FILM_MAKING = 'film_making'
    COOKING = 'cooking'
    OTHER = 'other'

    CREW_CHOICES = (
        (SOLO, 'solo'),
        (SMALL, 'small'),
        (LARGE, 'large'),
    )

    CAMERA_CHOICES = (
        (CANON, 'canon'),
        (NIKON, 'nikon'),
        (SONY, 'sony'),
        (PANASONIC, 'panasonic'),
        (FUJI, 'fuji'),
        (RED, 'red'),
        (OTHER, 'other'),
    )

    CATEGORY_CHOICES = (
        (CODE, 'code'),
        (REVIEWS, 'reviews'),
        (VLOGS, 'vlogs'),
        (COMEDY, 'comedy'),
        (GAMING, 'gaming'),
        (FILM_MAKING, 'film_making'),
        (COOKING,  'cooking'),
        (OTHER, 'other'),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='youtubers/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(
        max_length=255, choices=CREW_CHOICES, default=SOLO)
    camera_type = models.CharField(
        max_length=255, 	choices=CAMERA_CHOICES, default=CANON)
    subcribers = models.IntegerField()
    category = models.CharField(
        max_length=255, choices=CATEGORY_CHOICES, default=COMEDY)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
