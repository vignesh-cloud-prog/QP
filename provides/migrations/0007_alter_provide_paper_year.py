# Generated by Django 3.2 on 2021-09-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provides', '0006_auto_20210905_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provide',
            name='paper_year',
            field=models.DateField(),
        ),
    ]
