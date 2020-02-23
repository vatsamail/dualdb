from django.contrib import admin

# Register your models here.
# from .models import Post, Category
from .models import Content, Genre

# class PostAdmin(admin.ModelAdmin):
#     pass
#
# class CategoryAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)


class ContentAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Content, ContentAdmin)
admin.site.register(Genre, GenreAdmin)
