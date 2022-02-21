# Generated by Django 3.2.10 on 2022-02-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_paper',
            name='paper_type',
            field=models.SlugField(choices=[('board', 'board'), ('university', 'university')], help_text='Different levels of schools and colleges like Board and University', max_length=12),
        ),
    ]
