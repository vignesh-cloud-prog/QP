# Generated by Django 3.2 on 2021-06-01 08:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question_papers', '0004_remove_provider_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question_papers',
            new_name='Question_paper',
        ),
    ]