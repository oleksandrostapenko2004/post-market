# Generated by Django 4.2.2 on 2023-06-21 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stamps', '0009_alter_news_options_news_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='content',
            new_name='n_content',
        ),
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
    ]
