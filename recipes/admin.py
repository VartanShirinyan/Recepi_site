from django.contrib import admin
from .models import Recipe, Category, Ingredient, UserProfile

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(UserProfile)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
