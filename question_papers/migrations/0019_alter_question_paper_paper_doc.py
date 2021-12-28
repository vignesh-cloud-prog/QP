# Generated by Django 3.2.10 on 2021-12-24 17:23

import cloudinary_storage.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0018_auto_20211224_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_paper',
            name='paper_doc',
            field=models.FileField(help_text='The actual paper documnet', storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='qpweb_dev', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]