# Generated by Django 3.1.2 on 2020-12-03 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='comment',
            name='company',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.CharField(default='1', max_length=1),
        ),
    ]