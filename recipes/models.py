from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание")
    ingredients = models.TextField(verbose_name="Ингредиенты")
    steps = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.PositiveIntegerField(verbose_name="Время приготовления (мин)")
    image = models.ImageField(upload_to='recipes/', verbose_name="Изображение", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    categories = models.ManyToManyField(Category, related_name="recipes", verbose_name="Категории")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
