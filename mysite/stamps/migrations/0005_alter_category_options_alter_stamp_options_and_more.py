# Generated by Django 4.2.2 on 2023-06-18 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stamps', '0004_stamp_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='stamp',
            options={'ordering': ['title'], 'verbose_name': 'Топ марки', 'verbose_name_plural': 'Топ марки'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Категорії'),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stamps.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='content',
            field=models.TextField(blank=True, verbose_name='Детальна інформація'),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='in_stock',
            field=models.BooleanField(default=True, verbose_name='У наявності'),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='photos',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='price',
            field=models.TextField(blank=True, verbose_name='Ціна'),
        ),
        migrations.AlterField(
            model_name='stamp',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Заголовок'),
        ),
    ]