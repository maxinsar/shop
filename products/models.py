from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название категории")
    slug = models.SlugField(max_length=40, verbose_name="Ссылка")

    def __str__(self):
        return "Категория {0}".format(self.name)

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    class Meta:
        verbose_name="Категорию"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название товара")
    slug = models.SlugField(max_length=60, verbose_name="Ссылка")
    description = models.CharField(max_length=400, verbose_name="Описание")
    price = models.DecimalField(max_digits = 10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to = "image/product", verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория товара")
    aviable = models.BooleanField(default=False, verbose_name="В наличии")

    def __str__(self):
        return "Товар {0}".format(self.name)

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
