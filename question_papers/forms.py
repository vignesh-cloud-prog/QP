from django import forms

from .models import Provider,Issues

class ProviderForm(forms.Form):
    # name=forms.CharField(max_length=20,label='Your Name')
    # email=forms.CharField(max_length=100,label='Your Email Address')
    PAPER_CHOICES=(('board','Board'),('university','University'))
    paper_type=forms.ChoiceField(choices=PAPER_CHOICES)
    board=forms.CharField(max_length=100,label='Board / University')
    claass=forms.CharField(max_length=100,label='Course')
    sem=forms.CharField(max_length=100,label='Class / Semister')
    sub=forms.CharField(max_length=100,label='Subject')
    papertitle=forms.CharField(max_length=100,label='Paper Title / Examination')
    doc=forms.FileField(label='Document')

        

class issueForm(forms.ModelForm):
    
    class Meta:
        model = Issues
        fields = ['name',
                'email', 
                'phone',
                'issues',
                ]
