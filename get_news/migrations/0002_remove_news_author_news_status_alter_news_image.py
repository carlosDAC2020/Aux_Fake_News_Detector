# Generated by Django 4.1.7 on 2023-03-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.URLField(default=None, max_length=300),
        ),
    ]
