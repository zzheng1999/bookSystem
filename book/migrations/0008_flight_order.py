# Generated by Django 2.2.4 on 2019-09-11 18:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0007_auto_20190911_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('departure_city', models.CharField(max_length=100, null=True)),
                ('arrive_city', models.CharField(max_length=100, null=True)),
                ('departure_airport', models.CharField(max_length=100, null=True)),
                ('arrive_airport', models.CharField(max_length=100, null=True)),
                ('departure_time', models.DateTimeField(null=True)),
                ('arrive_time', models.DateTimeField(null=True)),
                ('capacity', models.IntegerField(default=0, null=True)),
                ('price', models.FloatField(default=0, null=True)),
                ('book_sum', models.IntegerField(default=0, null=True)),
                ('distance', models.FloatField(default=0, null=True)),
                ('user', models.ManyToManyField(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
