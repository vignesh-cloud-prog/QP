# Generated by Django 3.2.10 on 2021-12-24 17:21

import cloudinary_storage.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provides', '0017_alter_provide_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provide',
            name='doc',
            field=models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='providers_dev', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]