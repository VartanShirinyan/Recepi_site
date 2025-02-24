from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Recipe, Category, Ingredient, UserProfile
from .forms import RecipeForm, CategoryForm, IngredientForm, UserProfileForm, RecipeSearchForm
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

def home(request):
    # Получаем 5 случайных рецептов
    random_recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'recipes/home.html', {'recipes': random_recipes})

# views.py
def all_recipes(request):
    form = RecipeSearchForm(request.GET)
    recipes = Recipe.objects.all().order_by('-created_at')  # Сортировка по дате создания (новые сначала)
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')
        ingredient = form.cleaned_data.get('ingredient')

        if query:
            recipes = recipes.filter(title__icontains=query)
        if category:
            recipes = recipes.filter(categories=category)
        if ingredient:
            recipes = recipes.filter(ingredients=ingredient)

    # Пагинация
    paginator = Paginator(recipes, 10)  # 10 рецептов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/all_recipes.html', {'page_obj': page_obj, 'form': form})

# Просмотр деталей рецепта
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Добавление рецепта
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            messages.success(request, 'Рецепт успешно добавлен!')
            return redirect('recipes:home')
        else:
            print("Ошибки формы:", form.errors)  # Отладочный вывод
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

# Добавление ингредиента
@login_required
def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:add_recipe')  # Перенаправляем обратно на страницу добавления рецепта
    else:
        form = IngredientForm()
    return render(request, 'recipes/add_ingredient.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:add_recipe')  # Перенаправляем обратно на страницу добавления рецепта
    else:
        form = CategoryForm()
    return render(request, 'recipes/add_category.html', {'form': form})

# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('recipes:home')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/register.html', {'form': form})

# Профиль пользователя
@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('recipes:profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'recipes/profile.html', {'form': form})


# views.py
@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_detail', pk=recipe.id)  # Используем pk вместо recipe_id
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    recipe.delete()
    messages.success(request, 'Рецепт удален!')
    return redirect('recipes:home')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/list.html', {'recipes': recipes})


def upload_image(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'upload.html', {'form': form})
