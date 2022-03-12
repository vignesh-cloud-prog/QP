# Generated by Django 3.2.10 on 2022-01-29 18:14

import cloudinary_storage.storage
import django.core.validators
from django.db import migrations, models
import provides.models


class Migration(migrations.Migration):

    dependencies = [
        ('provides', '0018_alter_provide_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provide',
            name='doc',
            field=models.FileField(max_length=300, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to=provides.models.update_filename_and_path_dev, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]