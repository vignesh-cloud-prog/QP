from django.shortcuts import render
from .forms import ProvideForm
from django.contrib import messages
from django.core.mail import send_mail
from question_papers.models import Question_paper
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
    governing_body_list=Question_paper.objects.values('governing_body').distinct()
    course_name_list=Question_paper.objects.values('course_name').distinct()
    subject_name_list=Question_paper.objects.values('subject_name').distinct()

    providers = {
        'governing_body_list':governing_body_list,
        'course_name_list':course_name_list,
        'subject_name_list':subject_name_list,
        'form': ProvideForm
    }
    print(type(request.POST))
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
                send_mail(
                    f'A new question paper by {request.user.username}',
                    f"The paper provided by {request.user.email} and you can check on the website ➡ https://qpweb.herokuapp.com/push.",
                    'qpcom80@gmail.com',
                    ['vigneshun80@gmail.com'],
                    fail_silently=True,
                    )
                providers["form"] = ProvideForm()

            except Exception as e:
                print(request.POST)
                providers["form"] = ProvideForm(initial=(request.POST.dict()))
                messages.error(request, f"something went wrong! ({e})")
        else:
            print(request.POST)
            providers["form"] = ProvideForm(initial=(request.POST.dict()))
            messages.warning(request,  form.errors)

    

    return render(request, 'provides/provide.html', providers)
