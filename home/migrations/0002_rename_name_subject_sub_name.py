# Generated by Django 3.2.4 on 2022-02-05 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='sub_name',
        ),
    ]