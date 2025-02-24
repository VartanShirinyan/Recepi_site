from django import forms
from .models import Recipe, Category, Ingredient, UserProfile

class RecipeForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1}),
        label='Описание'
    )
    preparation_steps = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1}),
        label='Шаги приготовления'
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'cooking_time', 'image', 'categories', 'ingredients']

class RecipeSearchForm(forms.Form):
    query = forms.CharField(label='Поиск по названию', required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        required=False,
        empty_label="Все"  # Заменяем прочерк на "Все"
    )
    
    # Поле для выбора ингредиента с меткой "Все"
    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        label='Ингредиент',
        required=False,
        empty_label="Все"  # Заменяем прочерк на "Все"
    )

    def clean(self):
        cleaned_data = super().clean()
        preparation_steps = cleaned_data.get('preparation_steps')
        
        # Проверка длины шагов приготовления
        if preparation_steps and len(preparation_steps) < 10:
            self.add_error(
                'preparation_steps',
                'Шаги приготовления должны содержать не менее 10 символов.'
            )
        
        # Проверка времени приготовления
        cooking_time = cleaned_data.get('cooking_time')
        if cooking_time and cooking_time <= 0:
            self.add_error(
                'cooking_time',
                'Время приготовления должно быть больше 0.'
            )
        
        return cleaned_data
    
    
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