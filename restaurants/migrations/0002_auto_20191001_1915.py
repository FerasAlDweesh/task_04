# Generated by Django 2.1.5 on 2019-10-01 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='cusine',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='delivery',
        ),
    ]
