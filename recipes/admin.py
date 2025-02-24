from django.contrib import admin
from .models import Recipe, Category, UserProfile

admin.site.register(Category)
admin.site.register(UserProfile)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
