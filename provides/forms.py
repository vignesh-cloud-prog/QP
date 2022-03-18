from django import forms
from .models import Provide
from .utils import file_size,yearsago
from datetime import datetime


def doc_size(value):
    file_size(value, size=5)


class ProvideForm(forms.ModelForm):
    doc = forms.FileField(required=True, validators=[doc_size],widget=forms.FileInput(attrs={'type': "file", 'accept': "application/pdf", }),)

    # def clean_paper_year(self):
    #     date = self.cleaned_data['paper_year']
    #     if(date > datetime.now().date() or date < yearsago(3)):
    #         raise forms.ValidationError(
    #             message="Date cannot be in future and less than 3 year ago")

    class Meta:
        model = Provide
        fields = '__all__'
        exclude = ['provider', 'provider_email', 'provided_date', 'id']
        labels = {
            'doc': ("Document"),
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
            'paper_type': forms.Select(attrs={'class': 'form-control', }),
            'paper_year': forms.DateInput(attrs={'type': 'date','max':datetime.now().date(),'min':yearsago(5), }),
            'governing_body': forms.TextInput(attrs={'placeholder': 'Ex: Magalore University'}),
            'course_name': forms.TextInput(attrs={'placeholder': 'Ex: BCA'}),
            'subject_name': forms.TextInput(attrs={'placeholder': 'Ex: Python'}),
            'paper_title': forms.TextInput(attrs={'placeholder': 'Ex: Semister Examination'}),
        }
