# Generated by Django 3.1.2 on 2020-11-28 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201128_0911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='work_samples',
            new_name='website',
        ),
    ]
