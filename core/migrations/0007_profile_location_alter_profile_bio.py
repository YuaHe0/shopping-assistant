# Generated by Django 4.2 on 2023-05-09 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='', max_length=500),
        ),
    ]