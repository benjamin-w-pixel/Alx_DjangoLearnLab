# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from  .models import Tag 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 3
            })
        }
class TagWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value:
            tags = ', '.join([tag.name for tag in value.all()])
            value = tags
        return super().render(name, value, attrs, renderer)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',tags]
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]