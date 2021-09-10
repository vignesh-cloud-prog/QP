from django import forms
from .models import Provide

class ProvideForm(forms.ModelForm):
    class Meta:
        model = Provide
        fields = '__all__'
        exclude = ['provider','provided_date','id']
        labels={
            'doc':("Document"),
        }
        help_texts = {
            'name': ('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': ("This writer's name is too long."),
            },
        }
        widgets = {
            'paper_type': forms.Select(attrs={'class': 'form-control',}),
            'paper_year': forms.DateInput(attrs={'type': 'date',}),
            'course_name': forms.TextInput(attrs={}),
            'doc': forms.FileInput(attrs={'type':"file", 'accept':"application/pdf",}),
        }

