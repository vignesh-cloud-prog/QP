# Generated by Django 3.2 on 2021-12-05 18:18

import cloudinary_storage.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0016_alter_question_paper_paper_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_paper',
            name='paper_doc',
            field=models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='qpweb', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
