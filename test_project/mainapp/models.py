from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    image = models.ImageField(upload_to="products images", blank=True)
    short_desc = models.CharField(verbose_name="кратко", max_length=64, blank=True)
    description = models.TextField(verbose_name="подробно", blank=True)
    price = models.DecimalField(verbose_name="цена продукта", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="количество на складе", default=0)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)
