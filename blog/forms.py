from django import forms
from blog.models import Category
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=False)
class CategoryForm(forms.ModelForm):
    category = forms.CharField(required=False)
    class Meta:
        model = Category
        fields = ['category',]

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a comment!'
        }
    ))