# Generated by Django 2.0.3 on 2018-04-01 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0002_auto_20180401_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleuser',
            name='phoneNumber',
            field=models.CharField(default='NULL', max_length=55),
        ),
        migrations.AddField(
            model_name='vehicleuser',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehicleuser',
            name='UID',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AlterField(
            model_name='vehicleuser',
            name='reg_no',
            field=models.CharField(default=None, max_length=55),
        ),
    ]