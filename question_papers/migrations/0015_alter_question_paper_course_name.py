# Generated by Django 3.2 on 2021-09-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0014_alter_question_paper_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_paper',
            name='course_name',
            field=models.SlugField(default='board', max_length=800),
        ),
    ]