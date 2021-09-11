# Generated by Django 3.2 on 2021-07-20 10:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_type', models.CharField(choices=[('Board', 'Board'), ('University', 'University')], max_length=12)),
                ('college', models.CharField(max_length=100)),
                ('board', models.CharField(max_length=100)),
                ('claass', models.CharField(max_length=100)),
                ('sem', models.CharField(max_length=100)),
                ('sub', models.CharField(max_length=100)),
                ('papertitle', models.CharField(max_length=100)),
                ('doc', models.FileField(upload_to='provider')),
                ('provide_date', models.DateTimeField(default=datetime.datetime.now)),
                ('name', models.ForeignKey(blank=True, default='user', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]