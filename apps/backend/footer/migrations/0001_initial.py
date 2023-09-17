# Generated by Django 4.2.5 on 2023-09-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name_plural': ' Footer ',
                'db_table': 'footer',
            },
        ),
    ]