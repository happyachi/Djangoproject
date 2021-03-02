# Generated by Django 3.0.7 on 2020-09-21 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200917_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_photo', to='blog.Article'),
        ),
    ]
