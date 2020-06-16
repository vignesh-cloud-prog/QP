from django.shortcuts import render, HttpResponse
from .models import Question_papers,Issues,Provider
from django.http import request
from django.contrib import messages
from django.core.mail import send_mail
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
    
    return render(request,'question_papers/provide.html',providers
    )


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
        # paper=request.POST['paper']
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

    def text(

    ):
        
        return render('question_papers/share.html',text)



    


    # TWITTER_ENDPOINT = 'https://twitter.com/intent/tweet?text=%s'
# FACEBOOK_ENDPOINT = 'https://www.facebook.com/sharer/sharer.php?u=%s'
# GPLUS_ENDPOINT = 'https://plus.google.com/share?url=%s'
# MAIL_ENDPOINT = 'mailto:?subject=%s&body=%s'
# LINKEDIN_ENDPOINT = 'https://www.linkedin.com/shareArticle?mini=true&title=%s&url=%s'
# REDDIT_ENDPOINT = 'https://www.reddit.com/submit?title=%s&url=%s'
# TELEGRAM_ENDPOINT = 'https://t.me/share/url?text=%s&url=%s'
# WHATSAPP_ENDPOINT = 'https://api.whatsapp.com/send?text=%s'