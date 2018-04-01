# Generated by Django 2.0.3 on 2018-04-01 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0003_auto_20180401_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='PUC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(auto_now_add=True)),
                ('months', models.CharField(max_length=55)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.VehicleUser')),
            ],
        ),
    ]
