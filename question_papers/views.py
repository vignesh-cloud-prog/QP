from django.shortcuts import render, HttpResponse
from .models import Question_papers,Issues,Provider
from django.http import request,HttpRequest
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ProviderForm,issueForm
from django.core import serializers

# Create your views here.

def filter_first_option(request):
    college=Question_papers.objects.order_by('college').distinct('college')
    qs_json=serializers.serialize('json',college)
    return HttpResponse(qs_json,content_type='application/json')

def colleges(request):
    allqp=Question_papers.objects.order_by('college').distinct('college')
    context={'allqp' : allqp,'Select':'Select Your Current Education : '}
    print(allqp)
    return render(request,'question_papers/colleges.html',context)

def college(request,college):
    if college.startswith("json"):
        college=college.split("-")[1]
        college=Question_papers.objects.filter(college=college).order_by('university').distinct('university')
        qs_json=serializers.serialize('json',college)
        return HttpResponse(qs_json,content_type='application/json')


    college=Question_papers.objects.filter(college=college).order_by('university').distinct('university')
    college={'college' : college}
    return render(request,'question_papers/universities.html',college)

def university(request,college,university):
    if college.startswith("json"):
        college=college.split("-")[1]
        university=Question_papers.objects.filter(university=university,college=college).order_by('course').distinct('course')
        qs_json=serializers.serialize('json',university)
        return HttpResponse(qs_json,content_type='application/json')
    university=Question_papers.objects.filter(university=university,college=college).order_by('course').distinct('course')
    university={'university' : university}
    return render(request,'question_papers/courses.html',university)

def course(request,college,university,course):
    if college.startswith("json"):
        college=college.split("-")[1]
        course=Question_papers.objects.filter(course=course, university=university).order_by('year').distinct('year')
        qs_json=serializers.serialize('json',course)
        return HttpResponse(qs_json,content_type='application/json')
    course=Question_papers.objects.filter(course=course, university=university).order_by('year').distinct('year')
    course={'course' : course}
    return render(request,'question_papers/classes.html',course)

 
def year(request,college,university,course,year):
    if college.startswith("json"):
        college=college.split("-")[1]
        year=Question_papers.objects.filter(course=course,university=university).order_by('subject').distinct('subject')
        qs_json=serializers.serialize('json',year)
        return HttpResponse(qs_json,content_type='application/json')
    year=Question_papers.objects.filter(course=course,university=university).order_by('subject').distinct('subject')
    year={'year':year}
    return render(request,'question_papers/subjects.html',year)

def question_papers(request,college,university,course,year,subject):
    papers=Question_papers.objects.filter(subject=subject,university=university)
    papers={'paper':papers}
    return render(request,'question_papers/papers.html',papers)


def provider(request):
    form=ProviderForm(request.GET)
    form = ProviderForm(request.POST or None ,request.FILES )
    if form.is_valid():
       
        name=request.user
        print(name)
        paper_type=form.cleaned_data.get("paper_type") 
        board=form.cleaned_data.get("board") 
        claass = form.cleaned_data.get("claass") 
        sem = form.cleaned_data.get("sem") 
        sub= form.cleaned_data.get("sub") 
        papertitle=form.cleaned_data.get("papertitle") 
        doc = form.cleaned_data.get("doc") 
        provide=Provider(paper_type=paper_type,name=name,board=board,claass=claass,sem=sem,sub=sub,papertitle=papertitle,doc=doc)
        provide.save()
        messages.success(request, 'Thank you, we will check and update it soon .')
        form=ProviderForm()
        
    providers={
        'form':ProviderForm
    }
    
    return render(request,'question_papers/provide.html',providers
    )


def filters(request):
    college=request.POST.get('college')
    university=request.POST.get('university')
    course=request.POST.get('course')
    year=request.POST.get('year')
    subject=request.POST.get('subject')
    filter_obj=Question_papers.objects.filter(college=college).filter(year=year).filter(course=course).filter(subject=subject).filter(university=university)
    filter_obj={'context':filter_obj}
    return render(request,'question_papers/filter.html',filter_obj)


def issues(request):
    form = issueForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Message has been succesfully sent.')
        form=issueForm()   
    Issues={'form':issueForm}
    return render(request,'question_papers/contact.html',Issues)


def push(request):
    pushes=Provider.objects.all()
    push={'pushes':pushes}
    return render(request,'question_papers/push.html',push)

def pushed(request):
    if request.method=='POST':
        print("posting")
        # provider=request.POST['pro']
        provider=request.POST['pro']
        college=request.POST['college']
        university=request.POST['university']
        course=request.POST['course']
        year=request.POST['semister']
        subject=request.POST['subject']
        examination=request.POST['examination']
        paper=request.POST['paper']
        date=request.POST['date']
        id=request.POST['id']
        emailid=request.POST['email']
        push=Question_papers(provider=provider,college=college,university=university,course=course,year=year,subject=subject,examination=examination,paper=paper)
        push.save()

        pull=Provider(id=id,name=Provider,email=emailid,level=college,board=university,claass=course,sem=year,sub=subject,papertitle=examination,doc=paper,provide_date=date)
        pull.delete()
        
        send_mail(
            'hello',
            'i am vignesh',
            'qpcom80@gmail.com',
            [emailid],
            fail_silently=True,
            
        )
        


        return render(request,'question_papers/push.html',)

def search(request):
    query=request.GET['query']
    query=query.lower()
    print(query)
    query=query.replace(" ","_")
    print(query)
    result=Question_papers.objects.filter(slug__icontains=query)
    result={'results':result}
    print(result)
    return render(request,'question_papers/search.html',result)



    


    # TWITTER_ENDPOINT = 'https://twitter.com/intent/tweet?text=%s'
# FACEBOOK_ENDPOINT = 'https://www.facebook.com/sharer/sharer.php?u=%s'
# GPLUS_ENDPOINT = 'https://plus.google.com/share?url=%s'
# MAIL_ENDPOINT = 'mailto:?subject=%s&body=%s'
# LINKEDIN_ENDPOINT = 'https://www.linkedin.com/shareArticle?mini=true&title=%s&url=%s'
# REDDIT_ENDPOINT = 'https://www.reddit.com/submit?title=%s&url=%s'
# TELEGRAM_ENDPOINT = 'https://t.me/share/url?text=%s&url=%s'
# WHATSAPP_ENDPOINT = 'https://api.whatsapp.com/send?text=%s'