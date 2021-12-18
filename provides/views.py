from django.shortcuts import render
from .forms import ProvideForm
from django.contrib import messages

# Create your views here.

# this function helps users to upload therir question papers to qpweb


def provider(request):
    """
    Question papers form which is provided by the user :model:`provides.Provide`.

    **Context**

    ``mymodel``
        An instance of :model:`provides.Provide`.

    **Template:**

    :template:`provides/provide.html`
    """
    if request.method == 'POST':
        form = ProvideForm(request.POST or None, request.FILES)
        if form.is_valid():
            try:
                provide = form.save()
                print(provide)
                provide.provider = request.user
                provide.provider_email = request.user.email
                provide.save()
                messages.success(
                    request, 'Thank you, we will check and update it soon .')
                form = ProvideForm()

            except Exception as e:
                messages.error(request, f"something went wrong! ({e})")
        else:
            messages.warning(request,  form.errors)

    providers = {
        'form': ProvideForm
    }

    return render(request, 'provides/provide.html', providers)
