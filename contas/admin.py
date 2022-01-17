from django.contrib import admin

# Register your models here.

from .models import Category, Post, Contact

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'update_at', 'image_table']
    readonly_fields = ('image_table',)
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','message']
    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
