# Generated by Django 2.2.4 on 2019-09-10 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_flight_first_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='first_book_sum',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='first_capacity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
