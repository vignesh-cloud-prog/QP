# Generated by Django 3.2 on 2021-12-05 14:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provides', '0012_alter_provide_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provide',
            name='doc',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]