# Generated by Django 2.0.7 on 2018-08-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20180812_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='birth_day',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='birth_month',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='birth_year',
            field=models.IntegerField(blank=True),
        ),
    ]