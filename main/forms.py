from .models import Matches, Articles
from django.forms import ModelForm, TextInput, DateTimeInput
from django import forms


# class MatchesForm(ModelForm):  # Create a form for match introduction data
#     class Meta:  # Form settings
#         model = Matches
#         fields = ['team1', 'team2', 'time']
#         widgets = {
#             'team1': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'First team',
#             }),
#             'team2': TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Second team',
#             }),
#             'time': DateTimeInput(attrs=({
#                 'type': 'datetime-local',
#                 'format': '%d/%m/%Y %H:%M',
#                 'class': 'form-control',
#                 'placeholder': 'Date and time of match',
#             })),
#         }


class ArticlesForm(ModelForm):
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
