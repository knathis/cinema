# Generated by Django 3.0 on 2019-12-15 01:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('duration', models.IntegerField(default=0, verbose_name='duration (minutes)')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.IntegerField()),
                ('start_date', models.DateTimeField(default=datetime.datetime(2019, 12, 14, 20, 26, 57, 644717))),
                ('end_date', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_office.Movie')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_office.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_seats', models.IntegerField(default=1, verbose_name='Number of seats')),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket_office.Showtime')),
            ],
        ),
    ]
