from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='category_name',
        max_length=64,
        unique=True
    )

    description = models.TextField(
        verbose_name='category_description',
        blank=True
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='category'
    )

    name = models.CharField(
        verbose_name='product_name',
        max_length=64,
        unique=True
    )
    image = models.ImageField(
        upload_to='product_images',
        blank=True,
        verbose_name='product_image'
    )

    description = models.TextField(
        verbose_name='product_description',
        blank=True
    )

    short_desc = models.CharField(
        verbose_name='short description',
        max_length=100,
        blank=True
    )

    price = models.DecimalField(
        verbose_name='product_price',
        max_digits=8,
        decimal_places=2,
        default=0.0
    )

    quantity = models.PositiveIntegerField(
        verbose_name='product_quantity',
        default=0,
    )

    created_at = models.DateTimeField(
        verbose_name='created_at',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='updated_at',
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
