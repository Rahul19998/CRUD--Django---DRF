# Generated by Django 3.2 on 2021-05-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapi', '0004_auto_20210522_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
