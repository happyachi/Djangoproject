# Generated by Django 3.0.7 on 2020-09-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_picture_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='photo',
            field=models.ImageField(upload_to='image'),
        ),
    ]
