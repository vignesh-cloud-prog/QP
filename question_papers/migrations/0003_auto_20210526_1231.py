# Generated by Django 3.2 on 2021-05-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0002_provider_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='college',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='provider',
            name='paper_type',
            field=models.CharField(choices=[('board', 'Board'), ('university', 'University')], default='default', max_length=12),
            preserve_default=False,
        ),
    ]
