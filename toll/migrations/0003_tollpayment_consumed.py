# Generated by Django 2.0.3 on 2018-04-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toll', '0002_tollpayment_toll'),
    ]

    operations = [
        migrations.AddField(
            model_name='tollpayment',
            name='consumed',
            field=models.BooleanField(default=False),
        ),
    ]
