# Generated by Django 5.1.6 on 2025-03-04 19:50

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='recipes/'),
            preserve_default=False,
        ),
    ]
