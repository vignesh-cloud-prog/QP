# Generated by Django 3.0.6 on 2020-06-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0006_auto_20200623_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_papers',
            name='slug',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]