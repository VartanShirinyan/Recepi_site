from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Category, Ingredient, Recipe

class RecipeTests(TestCase):
    def setUp(self):
        # Создаем пользователя для тестов
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test description',
            preparation_steps='Steps here...',
            cooking_time=30,
            author=self.user  # Указываем автора
        )
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.author, self.user)  # Проверяем, что автор установлен
        
        
    def test_home_page(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)


    def test_recipe_with_categories_and_ingredients(self):
        category = Category.objects.create(name='Test Category')
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test description',
            preparation_steps='Steps here...',
            cooking_time=30,
            author=self.user
        )
        recipe.categories.add(category)
        recipe.ingredients.add(ingredient)
        self.assertEqual(recipe.categories.count(), 1)
        self.assertEqual(recipe.ingredients.count(), 1)