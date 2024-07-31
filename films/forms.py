from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'duration', 'director', 'is_active', 'image']
        widgets = {
            'duration': forms.TextInput(attrs={'placeholder': 'Enter duration in HH:MM:SS'}),
        }
