# Generated by Django 4.2 on 2024-06-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gourmet', '0007_category_name_alter_category_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('1', '和食'), ('2', '中華'), ('3', 'イタリアン'), ('4', 'フレンチ'), ('5', '寿司'), ('6', '焼肉'), ('7', '韓国料理')], max_length=50, verbose_name='ジャンル'),
        ),
    ]
