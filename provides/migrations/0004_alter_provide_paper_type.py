# Generated by Django 3.2 on 2021-07-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provides', '0003_auto_20210720_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provide',
            name='paper_type',
            field=models.CharField(choices=[('board', 'board'), ('university', 'university'), ('competitive', 'competitive')], max_length=12),
        ),
    ]
