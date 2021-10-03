from django.contrib import admin
from .models import Article, Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user', 'public', 'created_at')
    list_filter = ('public', 'user__username', 'categories__name')

    def save_model(self, request, object, form, change):
        if not object.user_id:
            object.user_id = request.user.id

        object.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)