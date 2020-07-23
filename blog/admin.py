from django.contrib import admin
from blog.models import Post, Category, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_body','created_on')
    pass

class CategoryAdmin(admin.ModelAdmin):

    pass
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created_on')
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)