# Generated by Django 3.2.4 on 2022-02-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_name_subject_sub_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualities',
            name='intern',
        ),
        migrations.AddField(
            model_name='qualities',
            name='quality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='intern',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='is_paper',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
