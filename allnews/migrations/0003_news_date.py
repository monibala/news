# Generated by Django 4.0.5 on 2022-10-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allnews', '0002_remove_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
