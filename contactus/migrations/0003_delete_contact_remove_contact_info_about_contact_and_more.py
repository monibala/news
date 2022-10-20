# Generated by Django 4.1.1 on 2022-10-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0002_rename_msg_contact_msg_remove_contact_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contact',
        ),
        migrations.RemoveField(
            model_name='contact_info',
            name='about_contact',
        ),
        migrations.RemoveField(
            model_name='contact_info',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='contact_info',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='contact_info',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='contact_info',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact_info',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact_info',
            name='msg',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact_info',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact_info',
            name='subject',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
