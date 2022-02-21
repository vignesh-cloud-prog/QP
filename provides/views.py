from django.shortcuts import render,HttpResponse
from django.core import serializers
from django.db.models import Q
from question_papers.models import Question_paper
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

    providers = {
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

def filter_provide_form_ajax(request,*args,**qwargs):
    paper_type = request.GET.get('paper_type')
    print(paper_type)
    education_type = request.GET.get('education_type')
    # print(type)
    governing_body = request.GET.get('governing_body')
    course_name = request.GET.get('course_name')
    period = request.GET.get('period')
    # print(company)
    query = Q(paper_type=paper_type)
    if education_type:
        query = query & Q(education_type=education_type)
    if governing_body:
        query = query & Q(governing_body=governing_body)
    if course_name:
        query = query & Q(course_name=course_name)
    if period:
        query = query & Q(period=period)
    # print(query)
    papers = Question_paper.objects.filter(query)
    # print(vehical_names)
    data = serializers.serialize('json', papers)

    return HttpResponse(data, content_type='application/json')