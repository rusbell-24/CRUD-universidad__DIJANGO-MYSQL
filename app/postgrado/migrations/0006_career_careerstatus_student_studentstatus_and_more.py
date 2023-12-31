# Generated by Django 4.2.4 on 2023-08-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgrado', '0005_rename_career_course_career_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='careerStatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='studentStatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacherStatus',
            field=models.BooleanField(default=True),
        ),
    ]
