from pyexpat.errors import messages
from random import sample
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

def home(request):
    # Получаем все рецепты
    all_recipes = Recipe.objects.all()

    # Если рецептов больше 5, выбираем 5 случайных
    if len(all_recipes) >= 5:
        recipes = sample(list(all_recipes), 5)
    else:
        recipes = all_recipes

    return render(request, 'recipes/home.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()  # Сохраняем связи ManyToMany (категории)
            return redirect("recipe_detail", recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, "recipes/add_recipe.html", {"form": form})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/list.html', {'recipes': recipes})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно. Пожалуйста, войдите.')
            return redirect('recipes:login')  # Убедитесь, что используется правильное имя
    else:
        form = UserCreationForm()
    return render(request, 'recipes/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'recipes/profile.html')