# Generated by Django 4.0.5 on 2022-10-27 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allnews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
    ]
