# Generated by Django 4.2.6 on 2023-10-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_owner_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]