from django import forms
from .models import Product, ProductComments

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_image', 'product_description',)

        widgets = {
            'product_description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Post Description',
                    'rows': 25,
                    'cols': 100,
                }
            ),
        }


class ProductCommentsForm(forms.ModelForm):
    class Meta:
        model = ProductComments
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
                    "placeholder": 'Enter your comment here',
                    'rows': 10,
                    'cols': 80,
                }
            )

        }

