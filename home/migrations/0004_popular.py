# Generated by Django 4.1.1 on 2022-10-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('features', models.TextField()),
            ],
        ),
    ]
