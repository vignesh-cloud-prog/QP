from django.forms import ModelForm
from .models import Provider

class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'
        exclude = ['name','provide_date']

