from django.contrib import admin
from .models import Register


admin.site.register(Register)










# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'created_at')  # Fields to display in the admin list view
#     search_fields = ('name',)  # Add a search box for 'name'
#     list_filter = ('price',)  # Add a filter for 'price'

# # Register the model with custom admin settings
# admin.site.register(Product, ProductAdmin)