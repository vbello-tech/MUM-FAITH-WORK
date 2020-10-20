from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_description', 'post_image', 'body',)

        widgets = {
            'post_description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Post Description',
                    'rows': 15,
                    'cols': 100,
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Enter your blog post here',
                    'rows': 30,
                    'cols': 100,
                }
            )

        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'body',)

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Enter Your Name',
                    'rows': 20,
                    'cols': 70,
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Enter your blog post here',
                    'rows': 10,
                    'cols': 80,
                }
            )

        }