# Generated by Django 4.2.6 on 2023-10-19 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
    ]