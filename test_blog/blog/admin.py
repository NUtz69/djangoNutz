from django.contrib import admin
from blog.models import Post, Comment
# Video
from embed_video.admin import AdminVideoMixin
# Thumbnail
from sorl.thumbnail.admin import AdminImageMixin


# Video - Ckeditor
class PostAdmin(AdminVideoMixin, AdminImageMixin, admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
