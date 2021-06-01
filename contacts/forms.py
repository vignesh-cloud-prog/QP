from django.forms import ModelForm
from .models import Issue

class issuesForm(ModelForm):

    class Meta:
        model = Issue
        fields = ['name',
                  'email',
                  'phone',
                  'issues',
                  ]
