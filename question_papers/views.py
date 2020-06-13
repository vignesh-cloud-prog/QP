from django.shortcuts import render, HttpResponse
from .models import Question_papers,Issues,Provider
from django.http import request
from django.contrib import messages
from .forms import ProviderForm,issueForm

# Create your views here.
def uni():
    uni=Question_papers.objects.order_by('university').distinct('university')
    return uni

def coll():
    coll=Question_papers.objects.order_by('college').distinct('college')
    return coll

def subj():
    subj=Question_papers.objects.order_by('subject').distinct('subject')
    return subj

def co():
    co=Question_papers.objects.order_by('course').distinct('course')
    return co

def yea():
    yea=Question_papers.objects.order_by('year').distinct('year')
    return yea


def colleges(request):
    allqp=Question_papers.objects.order_by('college').distinct('college')
    context={'allqp' : allqp,'Select':'Select Your Current Education : ','coll':coll,'uni':uni,'co':co,'subj':subj,'yea':yea}
    return render(request,'question_papers/qp.html',context)

def college(request,college):
    college=Question_papers.objects.filter(college=college).order_by('university').distinct('university')
    college={'college' : college,'coll':coll,'uni':uni,'co':co,'subj':subj,'yea':yea}
    print(college)
    return render(request,'question_papers/qp.html',college)

def university(request,college,university):
    university=Question_papers.objects.filter(university=university,college=college).order_by('course').distinct('course')
    university={'university' : university,'coll':coll,'uni':uni,'co':co,'subj':subj,'yea':yea}
    print(university)
    return render(request,'question_papers/qp.html',university)

def course(request,college,university,course):
    course=Question_papers.objects.filter(course=course, university=university).order_by('year').distinct('year')
    course={'course' : course,'coll':coll,'uni':uni,'co':co,'subj':subj,'yea':yea}
    print(course)
    return render(request,'question_papers/qp.html',course)

 
def year(request,college,university,course,year):
    year=Question_papers.objects.filter(course=course,university=university).order_by('subject').distinct('subject')
    year={'year':year,'coll':coll,'uni':uni,'co':co,'subj':subj,'yea':yea}
    return render(request,'question_papers/qp.html',year)

def question_papers(request,college,university,course,year,subject):
    papers=Question_papers.objects.filter(subject=subject,university=university)
    papers={'paper':papers}
    return render(request,'question_papers/qp.html',papers)


def provider(request):
    form=ProviderForm(request.GET)
    form = ProviderForm(request.POST or None ,request.FILES )
    if form.is_valid():
        form.save()
        messages.success(request, 'Thank you, we will check and update it soon .')
        form=ProviderForm()
    providers={
        'form':ProviderForm
    }
    return render(request,'question_papers/provide.html',providers)


def filter(request):
    college=request.POST.get('college')
    print(college)
    university=request.POST.get('university')
    print(university)
    course=request.POST.get('course')
    year=request.POST.get('year')
    subject=request.POST.get('subject')
    filter=Question_papers.objects.filter(college=college,year=year,course=course, subject=subject,university=university)
    filter={'filter':filter}
    print(filter)
    return render(request,'question_papers/filter.html',filter)


def issues(request):
    form = issueForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Message has been succesfully sent.')
        form=issueForm()   
    Issues={'form':issueForm}
    return render(request,'question_papers/contact.html',Issues)

    

