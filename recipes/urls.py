from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

app_name = 'recipes'  # Указываем имя приложения для namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),  # Маршрут для регистрации
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
