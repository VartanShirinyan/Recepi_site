from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

app_name = 'recipes'  

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),

    # Детали рецепта
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),

    # Добавление, редактирование и удаление рецептов
    path('add/', views.add_recipe, name='add_recipe'),
    path('all/', views.all_recipes, name='all_recipes'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('add-ingredient/', views.add_ingredient, name='add_ingredient'),
    path('add-category/', views.add_category, name='add_category'),

    # Список рецептов
    path('list/', views.recipe_list, name='recipe_list'),

    # Авторизация и регистрация
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html',  # Необязательно
        next_page='recipes:home'), name='logout'),
    path('register/', views.register, name='register'),

    # Профиль пользователя
    path('profile/', views.profile, name='profile'), 
]

