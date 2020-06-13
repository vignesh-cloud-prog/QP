from django import forms

from .models import Provider,Issues

class ProviderForm(forms.ModelForm):
    
    class Meta:
        model = Provider
        fields = ['name',
                'email',
                'level', 
                'board',
                'claass',
                'sem', 
                'sub',
                'papertitle',
                'doc',
                ]

class issueForm(forms.ModelForm):
    
    class Meta:
        model = Issues
        fields = ['name',
                'email', 
                'phone',
                'issues',
                ]