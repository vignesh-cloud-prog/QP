# Generated by Django 3.2 on 2021-09-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provides', '0009_alter_provide_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='provide',
            name='provider_email',
            field=models.EmailField(default='vignesh@vig.com', max_length=254),
            preserve_default=False,
        ),
    ]
