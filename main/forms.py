from .models import Articles
from django.forms import ModelForm, DateTimeInput
from django import forms


class ArticlesForm(ModelForm):
    """Add form of Articles"""
    class Meta:
        model = Articles
        fields = ['text', 'time']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control art',
                'placeholder': 'Article',
            }),
            'time': DateTimeInput(attrs=({
                'type': 'datetime-local',
                'format': '%d/%m/%Y %H:%M',
                'class': 'form-control time',
                'placeholder': 'Date and time add',
            })),
        }
