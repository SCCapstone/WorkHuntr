# Generated by Django 3.1.2 on 2021-02-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20201203_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='status',
            field=models.CharField(choices=[('Strutting', 'Strutting'), ('Spotted', 'Spotted'), ('Claimed', 'Claimed'), ('Completed', 'Completed'), ('Payment Issued', 'Payment Issued')], default='Strutting', max_length=14),
        ),
    ]
