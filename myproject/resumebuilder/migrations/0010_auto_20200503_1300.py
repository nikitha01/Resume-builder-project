# Generated by Django 3.0.5 on 2020-05-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumebuilder', '0009_auto_20200502_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumetable',
            name='phone',
            field=models.IntegerField(),
        ),
    ]