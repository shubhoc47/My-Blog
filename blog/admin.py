from django.contrib import admin
from .models import Post, Author, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ('tag', 'author', 'date')
    list_display = ("title", "date", "author",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
