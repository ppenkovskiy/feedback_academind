# Generated by Django 4.2.6 on 2023-10-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='owner_comment',
            field=models.TextField(default=''),
        ),
    ]
