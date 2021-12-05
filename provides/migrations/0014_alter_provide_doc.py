# Generated by Django 3.2 on 2021-12-05 14:44

import cloudinary_storage.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provides', '0013_alter_provide_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provide',
            name='doc',
            field=models.ImageField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='provider', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
