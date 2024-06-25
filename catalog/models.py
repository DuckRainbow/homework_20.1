from django.db import models
from django import forms

from users.models import User


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
    price = models.PositiveIntegerField(verbose_name="Цена за покупку", blank=True, null=True)
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
    creator = models.ForeignKey(
        User,
        verbose_name='Создатель',
        help_text='Укажите создателя карточки продукта',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    published = models.BooleanField(
        verbose_name="Опубликована",
        blank=True,
        default=False,
    )

    def __str__(self):
        # Строковое отображение объекта
        return (
            f"Продукт {self.title} из категории {self.category}, стоимость {self.price}"
        )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [
            ("can_unpublish_product", "Can unpublish a product"),
            ("can_edit_description", "Can edit the description of any product"),
            ("can_change_category", "Can change the category of any product"),
        ]


class Article(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        blank=True,
        null=True,
        help_text='Введите заголовок статьи.'
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="slug",
        blank=True,
        null=True,
        help_text='Введите URL статьи.'
    )
    content = models.TextField(
        verbose_name="Содержимое",
        blank=True,
        null=True,
        help_text='Введите статью.'
    )
    preview = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Превью статьи",
        help_text='Добавьте изображение.'
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        blank=True,
        null=True
    )
    published = models.BooleanField(
        verbose_name="Опубликована",
        blank=True
    )
    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите количество просмотров',
        default=0
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.title}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='versions',
        on_delete=models.SET_NULL,
        verbose_name="Продукты данной версии",
        null=True,
        blank=True,
        help_text='Продукты данной версии:'
    )
    counter = models.PositiveIntegerField(
        verbose_name='Номер версии',
        help_text='Укажите номер версии.',
        default=1
    )
    title = models.CharField(
        max_length=50,
        verbose_name="Название версии",
        blank=True,
        null=True,
        help_text='Введите название версии.'
    )
    currented = models.BooleanField(
        verbose_name="Текущая версия",
        blank=True
    )

    def str(self):
        # Строковое отображение объекта
        return f"{self.title}"

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"
