# Generated by Django 3.0.7 on 2020-09-28 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200928_1540'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Picture',
        ),
    ]