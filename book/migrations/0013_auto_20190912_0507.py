# Generated by Django 2.2.4 on 2019-09-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_auto_20190911_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='bank_account',
            field=models.IntegerField(default=0),
        ),
    ]
