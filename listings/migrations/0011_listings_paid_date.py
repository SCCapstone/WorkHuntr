# Generated by Django 3.1.2 on 2021-02-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_merge_20210222_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='paid_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
