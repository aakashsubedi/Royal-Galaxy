# Generated by Django 4.2.5 on 2023-09-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='position',
            field=models.IntegerField(blank=True, null=True, verbose_name='Position'),
        ),
    ]
