# Generated by Django 3.2 on 2021-05-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapi', '0005_alter_courses_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image_path',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
