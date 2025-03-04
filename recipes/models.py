from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ингредиента')

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preparation_steps = models.TextField(verbose_name='Шаги приготовления')
    cooking_time = models.PositiveIntegerField(verbose_name='Время приготовления (минуты)')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    categories = models.ManyToManyField(Category, blank=True, verbose_name='Категории')
    ingredients = models.ManyToManyField(Ingredient, blank=True, verbose_name='Ингредиенты')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    image = ProcessedImageField(
        upload_to='recipes/',
        processors=[ResizeToFill(300, 200)],  # Размеры в пикселях
        format='JPEG',
        options={'quality': 90},
    )
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(blank=True, null=True, verbose_name='О себе')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name='Фото профиля')

    def __str__(self):
        return f'Профиль {self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

