# Generated by Django 3.0.5 on 2020-05-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumebuilder', '0007_resumetable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumetable',
            old_name='experience',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='resumetable',
            old_name='pro_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='resumetable',
            old_name='pro_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='resumetable',
            name='education',
        ),
        migrations.AddField(
            model_name='resumetable',
            name='marks_1',
            field=models.DecimalField(decimal_places=2, default=11, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumetable',
            name='marks_2',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumetable',
            name='marks_3',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumetable',
            name='puc',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resumetable',
            name='school',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
