# Generated by Django 4.2.4 on 2023-10-12 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversionesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='date',
            field=models.CharField(default='none', max_length=15),
        ),
        migrations.AddField(
            model_name='simulation',
            name='time',
            field=models.CharField(default='none', max_length=15),
        ),
    ]
