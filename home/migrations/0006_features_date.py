# Generated by Django 4.1.1 on 2022-10-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_features_remove_popular_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='features',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
