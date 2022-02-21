from django.shortcuts import render
from .forms import issuesForm
from django.contrib import messages

# Create your views here.
def issues(request):
    """
    Used to take issues from the users.

    **Context**

    ``mymodel``
        An instance of :model:`contacts.Issue`.

    **Template:**

    :template:`contacts/contact.html`
    """
    form = issuesForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Message has been succesfully sent.')
        form = issuesForm()
    Issues = {'form': issuesForm}
    return render(request, 'contacts/contact.html', Issues)
