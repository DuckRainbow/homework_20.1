# Generated by Django 4.2.11 on 2024-05-06 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="catalog/image",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Цена за покупку"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата последнего изменения"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="catalog",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
