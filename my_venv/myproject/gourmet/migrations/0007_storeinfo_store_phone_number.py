# Generated by Django 4.2 on 2024-09-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gourmet', '0006_storeinfo_store_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeinfo',
            name='store_phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='店舗電話番号'),
        ),
    ]
