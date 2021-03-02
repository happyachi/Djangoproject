# Generated by Django 3.0.7 on 2020-09-15 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='article_photo', to='blog.Article'),
        ),
    ]
