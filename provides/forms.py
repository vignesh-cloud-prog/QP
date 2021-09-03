from django.forms import ModelForm
from .models import Provide

class ProvideForm(ModelForm):
    class Meta:
        model = Provide
        fields = '__all__'
        exclude = ['provider','provide_date','id']

