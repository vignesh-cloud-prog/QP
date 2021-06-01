from django.shortcuts import render
from .forms import issuesForm
from django.contrib import messages

# Create your views here.
# Isuues are given here
def issues(request):
    form = issuesForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Message has been succesfully sent.')
        form = issuesForm()
    Issues = {'form': issuesForm}
    return render(request, 'contacts/contact.html', Issues)
