from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    search_fields = ("title", "author",)


admin.site.unregister(models.Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

# Register your models here.
