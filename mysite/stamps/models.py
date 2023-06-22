from django.db import models

# Create your models here.
from django.urls import reverse


class Stamp(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name="URL")
    price = models.TextField(blank=True, verbose_name="Ціна")
    content = models.TextField(blank=True, verbose_name="Детальна інформація")
    photos = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    in_stock = models.BooleanField(default=True, verbose_name="У наявності")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категорія")
    # email = models.EmailField(max_length=255)
    # order_number = models.TextField(max_length=8)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Топ марки'
        verbose_name_plural = 'Топ марки'
        ordering = ['-in_stock', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорії")
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id']

class News(models.Model):
    news_name = models.CharField(max_length=100, db_index=True, verbose_name="Новини")
    # slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name="URL")
    n_content = models.TextField(blank=True, verbose_name="Вміст новини")

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['id']