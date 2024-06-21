from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Наименование", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.title}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length=50, verbose_name="Наименование", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="catalog/image", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.PositiveIntegerField(verbose_name="Цена за покупку", blank=True, null=True)
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения", auto_now=True
    )

    def __str__(self):
        # Строковое отображение объекта
        return (
            f"Продукт {self.title} из категории {self.category}, стоимость {self.price}"
        )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
