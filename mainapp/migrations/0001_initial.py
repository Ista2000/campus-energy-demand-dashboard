# Generated by Django 2.2.6 on 2019-11-09 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.DecimalField(decimal_places=3, default=0, max_digits=7)),
                ('humidity', models.DecimalField(decimal_places=3, default=0, max_digits=7)),
                ('energy_1', models.DecimalField(decimal_places=3, default=0, max_digits=13)),
                ('energy_2', models.DecimalField(decimal_places=3, default=0, max_digits=13)),
                ('energy_3', models.DecimalField(decimal_places=3, default=0, max_digits=13)),
                ('energy_4', models.DecimalField(decimal_places=3, default=0, max_digits=13)),
                ('energy_5', models.DecimalField(decimal_places=3, default=0, max_digits=13)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
