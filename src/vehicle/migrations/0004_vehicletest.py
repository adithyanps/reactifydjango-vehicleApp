# Generated by Django 2.0.6 on 2018-11-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicletest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_no', models.CharField(max_length=120)),
                ('value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]