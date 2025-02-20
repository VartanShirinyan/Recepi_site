from django import forms
from .models import Recipe, Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "steps",
            "cooking_time",
            "image",
            "categories",
        ]
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления (в минутах)',
            'category': 'Категория',
            'image': 'Изображение',
            'categories': 'Категории'
        }
        widgets = {
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']