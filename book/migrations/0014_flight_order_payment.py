# Generated by Django 2.2.4 on 2019-09-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20190912_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight_order',
            name='payment',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
