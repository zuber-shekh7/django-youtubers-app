# Generated by Django 2.2 on 2021-07-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('nikon', 'nikon'), ('sony', 'sony'), ('panasonic', 'panasonic'), ('fuji', 'fuji'), ('red', 'red'), ('other', 'other')], default='canon', max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('reviews', 'reviews'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('film_making', 'film_making'), ('cooking', 'cooking'), ('other', 'other')], default='comedy', max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], default='solo', max_length=255),
        ),
    ]
