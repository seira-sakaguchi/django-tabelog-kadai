# Generated by Django 4.2 on 2024-06-21 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gourmet', '0004_remove_category_category_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeinfo',
            name='category',
        ),
    ]
