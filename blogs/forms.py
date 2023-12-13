from django import forms
from . import models


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        labels = {'text': ''}
        fields = ['title', 'text']
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
