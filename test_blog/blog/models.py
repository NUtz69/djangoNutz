from django.db import models
from django.utils import timezone
from django.urls import reverse
# Ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
# Embed_video
from embed_video.fields import EmbedVideoField
# Thumbnail
from sorl.thumbnail import ImageField


# Post
class Post(models.Model):
    # User
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Title
    title = models.CharField(max_length=200)
    # Text
    # text = RichTextUploadingField(default='', blank=True)
    text = RichTextUploadingField()
    # Create Date time
    created_date = models.DateTimeField(default=timezone.now)  # TZ sans ()
    # Published Date
    published_date = models.DateTimeField(blank=True, null=True)
    # Video
    # video = EmbedVideoField(default='', blank=True)
    video = EmbedVideoField()
    # Thumbnail
    # image = ImageField(default='', blank=True)
    image = ImageField(default='', blank=True)

    # Meta
    class Meta:
      verbose_name_plural = "posts"

    # Method published
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Method approve comments
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)  # Approved comment

    # Method reverse url
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    # Show post
    def __str__(self):
        return self.title


# Comment
class Comment(models.Model):
    # Comment user to post
    post = models.ForeignKey('blog.Post', related_name='comments',
                             on_delete=models.CASCADE)
    # Author
    author = models.CharField(max_length=200)
    # Text
    text = RichTextUploadingField()
    # Create Date time
    created_date = models.DateTimeField(default=timezone.now)  # TZ sans ()
    # Approved comment
    approved_comment = models.BooleanField(default=False)

    # Method approve
    def approve(self):
        self.approved_comment = True
        self.save()

    # Method reverse url
    def get_absolute_url(self):
        return reverse('post_list')

    # Show comment
    def __str__(self):
        return self.text
