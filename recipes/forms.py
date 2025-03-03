from django import forms
from .models import Recipe, Category, Ingredient, UserProfile

class RecipeForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        label='Описание'
    )
    preparation_steps = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        label='Шаги приготовления'
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'cooking_time', 'image', 'categories', 'ingredients']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
            'categories': forms.CheckboxSelectMultiple(),
        }

class RecipeSearchForm(forms.Form):
    query = forms.CharField(label='Поиск по названию', required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        required=False,
        empty_label="Все"
    )
    
    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        label='Ингредиент',
        required=False,
        empty_label="Все"
    )

    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']