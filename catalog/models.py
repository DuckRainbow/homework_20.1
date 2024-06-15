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
        max_length=50,
        verbose_name="Наименование",
        blank=True,
        null=True,
        help_text='Введите наименование продукта.'
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text='Введите описание.'
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text='Добавьте изображение продукта.'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="catalog",
        help_text='Выберите категорию.'
    )
    price = models.IntegerField(verbose_name="Цена за покупку", blank=True, null=True)
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        blank=True,
        null=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения",
        blank=True,
        null=True
    )
    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите количество просмотров',
        default=0
    )
    published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True
    )

    def __str__(self):
        # Строковое отображение объекта
        return (
            f"Продукт {self.title} из категории {self.category}, стоимость {self.price}"
        )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
