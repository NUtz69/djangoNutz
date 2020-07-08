from django import forms
from django.contrib import admin
from blog.models import Post, Comment
# CKEditor
from ckeditor.widgets import CKEditorWidget



# Post form
class PostForm(forms.ModelForm):
    # Fields
    class Meta():
        model = Post
        # fields = '__all__'

        fields = ('author', 'title', 'text', 'video', 'image')
        # fields = ('author', 'title', 'text')

        # Widgets CSS
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # Ckeditor widget
            'text': forms.CharField(widget=CKEditorWidget()),
        }


# Comment form
class CommentForm(forms.ModelForm):
    # Fields
    class Meta():
        model = Comment
        fields = ('author', 'text')

        # Widgets CSS
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}), # CSS
            # Ckeditor widget
            'text': forms.CharField(widget=CKEditorWidget()),
        }
