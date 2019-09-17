# Generated by Django 2.2.4 on 2019-09-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_flight_distance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('distance', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('bank_account', models.CharField(max_length=20)),
            ],
        ),
    ]
