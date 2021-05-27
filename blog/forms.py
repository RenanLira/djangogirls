from django import forms
from django.forms import fields
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-form'}),
            'text': forms.Textarea(attrs={'class': 'text-form'})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'title-form'}),
            'text': forms.Textarea(attrs={'class': 'text-form'})
        }