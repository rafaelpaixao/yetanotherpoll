# Generated by Django 3.0.8 on 2020-07-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_guest',
            field=models.BooleanField(default=False, help_text='Guest users can author Polls and vote on public polls prior to registration.'),
        ),
    ]