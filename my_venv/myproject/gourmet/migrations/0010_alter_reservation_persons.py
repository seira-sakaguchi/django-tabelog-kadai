# Generated by Django 4.2 on 2024-07-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gourmet', '0009_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='persons',
            field=models.IntegerField(verbose_name='予約人数'),
        ),
    ]
