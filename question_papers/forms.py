from django.forms import ModelForm

from .models import Provider, Issues


class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'
        exclude = ['name','provide_date']


class issueForm(ModelForm):

    class Meta:
        model = Issues
        fields = ['name',
                  'email',
                  'phone',
                  'issues',
                  ]
