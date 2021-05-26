from django.shortcuts import render, HttpResponse, redirect
from .models import Question_papers, Issues, Provider
from django.http import request, HttpRequest
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ProviderForm, issueForm
from django.core import serializers
from examination.models import Profile
from django.contrib.auth.models import User
# Create your views here.

# this function returns distinct values for different college types for json responce
def filter_first_option(request):
    college = Question_papers.objects.order_by('college').distinct('college')
    qs_json = serializers.serialize('json', college)
    return HttpResponse(qs_json, content_type='application/json')

# this function returns distinct values for different college types 
def colleges(request):
    allqp = Question_papers.objects.order_by('college').distinct('college')
    context = {'allqp': allqp, 'Select': 'Select Your Current Education : '}
    return render(request, 'question_papers/colleges.html', context)

# this function returns distinct values for different universities and boards in college types 
def college(request, college):
    if college.startswith("json"):
        college = college.split("-")[1]
        college = Question_papers.objects.filter(
            college=college).order_by('university').distinct('university')
        qs_json = serializers.serialize('json', college)
        return HttpResponse(qs_json, content_type='application/json')

    college = Question_papers.objects.filter(
        college=college).order_by('university').distinct('university')
    college = {'college': college}
    return render(request, 'question_papers/universities.html', college)

# this function returns distinct values for different cousres in an universities
def university(request, college, university):
    if college.startswith("json"):
        college = college.split("-")[1]
        university = Question_papers.objects.filter(
            university=university, college=college).order_by('course').distinct('course')
        qs_json = serializers.serialize('json', university)
        return HttpResponse(qs_json, content_type='application/json')
    university = Question_papers.objects.filter(
        university=university, college=college).order_by('course').distinct('course')
    university = {'university': university}
    return render(request, 'question_papers/courses.html', university)

# this function returns distinct values for different semisters or years in an course
def course(request, college, university, course):
    if college.startswith("json"):
        college = college.split("-")[1]
        course = Question_papers.objects.filter(
            course=course, university=university).order_by('year').distinct('year')
        qs_json = serializers.serialize('json', course)
        return HttpResponse(qs_json, content_type='application/json')
    course = Question_papers.objects.filter(
        course=course, university=university).order_by('year').distinct('year')
    course = {'course': course}
    return render(request, 'question_papers/classes.html', course)

# this function returns distinct values for distinct different subjects in a semisters
def year(request, college, university, course, year):
    if college.startswith("json"):
        college = college.split("-")[1]
        year = Question_papers.objects.filter(
            course=course, university=university).order_by('subject').distinct('subject')
        qs_json = serializers.serialize('json', year)
        return HttpResponse(qs_json, content_type='application/json')
    year = Question_papers.objects.filter(
        course=course, university=university).order_by('subject').distinct('subject')
    year = {'year': year}
    return render(request, 'question_papers/subjects.html', year)

# this function returns distinct values for different distinct avilable years of papers of a particular subject
def question_papers(request, college, university, course, year, subject):
    papers = Question_papers.objects.filter(
        subject=subject, university=university)
    papers = {'paper': papers}
    return render(request, 'question_papers/papers.html', papers)


# this function helps users to upload therir question papers to qpweb
def provider(request):
    form = ProviderForm(request.POST or None, request.FILES)
    if form.is_valid():
        provide=form.save()
        print(provide)
        provide.name=request.user.id
        provide.save()        
        messages.success(request, 'Thank you, we will check and update it soon .')
        form = ProviderForm()

    providers = {
        'form': ProviderForm
    }

    return render(request, 'question_papers/provide.html', providers)

# this function returns filtered elements to a html page
def filters(request):
    college = request.POST.get('college')
    university = request.POST.get('university')
    course = request.POST.get('course')
    year = request.POST.get('year')
    subject = request.POST.get('subject')
    filter_obj = Question_papers.objects.filter(college=college).filter(year=year).filter(
        course=course).filter(subject=subject).filter(university=university)
    filter_obj = {'context': filter_obj}
    return render(request, 'question_papers/filter.html', filter_obj)

# Isuues are discussed here
def issues(request):
    form = issueForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Message has been succesfully sent.')
        form = issueForm()
    Issues = {'form': issueForm}
    return render(request, 'question_papers/contact.html', Issues)

# Function helps to get all the items need to be pushed which availed from provider function
def push(request):
    pushes = Provider.objects.all()
    push = {'pushes': pushes}
    return render(request, 'question_papers/push.html', push)

# function helps to upload and delete papers uploaded by users
def pushed(request):
    if request.method == 'POST':
        provider = request.POST['pro']
        paper_type= request.POST['paper_type']
        emailid=request.POST['email']
        college = request.POST['college']
        university = request.POST['university']
        course = request.POST['course']
        year = request.POST['semister']
        subject = request.POST['subject']
        examination = request.POST['examination']
        paper = request.POST['paper']
        date = request.POST['date']
        pro_id = request.POST['id']
        emailid = request.POST['email']
        push = Question_papers(provider=provider,paper_type=paper_type, college=college, university=university,
                               course=course, year=year, subject=subject, examination=examination, paper=paper)
        push.save()

        pull = Provider(id=pro_id, name=provider, email=emailid, level=college, board=university,
                        claass=course, sem=year, sub=subject, papertitle=examination, doc=paper, provide_date=date)
        pull.delete()

        send_mail(
            'hello',
            'i am vignesh',
            'qpcom80@gmail.com',
            [emailid],
            fail_silently=True,

        )

        return render(request, 'question_papers/push.html',)


def search(request):
    query = request.GET['query']
    query = query.lower()
    query = query.replace(" ", "_")
    result = Question_papers.objects.filter(slug__icontains=query)
    result = {'results': result}
    return render(request, 'question_papers/search.html', result)


def profile_settings(request):
    if request.method == "POST" or None or request.FILES:

        user_id = request.POST.get('user_id')
        name = request.POST.get('full_name')
        pic = request.FILES.get('pic')
        bio = request.POST.get('bio')
        college = request.POST.get('college')
        try:
            if name is "" or bio is "" or college == "":
                messages.warning(request, 'Values can not be null.')
                return render(request, 'accounts/profile_edit.html')

            userObj = User.objects.get(id=user_id)
            userObj.first_name = name
            userObj.save()

            profileObj = Profile.objects.get(user=request.user)

            profileObj.college = college
            if pic is not None:
                profileObj.pic = pic
            profileObj.bio = bio
            profileObj.save()
            messages.success(request, 'Your profile updated successfully.')

            return redirect("profile")
        except Exception as e:
            messages.error(request, f"Profile not updated successfully\n {e}")
            return render(request, 'accounts/profile_edit.html')

    return render(request, 'accounts/profile_edit.html')

# TWITTER_ENDPOINT = 'https://twitter.com/intent/tweet?text=%s'
# FACEBOOK_ENDPOINT = 'https://www.facebook.com/sharer/sharer.php?u=%s'
# GPLUS_ENDPOINT = 'https://plus.google.com/share?url=%s'
# MAIL_ENDPOINT = 'mailto:?subject=%s&body=%s'
# LINKEDIN_ENDPOINT = 'https://www.linkedin.com/shareArticle?mini=true&title=%s&url=%s'
# REDDIT_ENDPOINT = 'https://www.reddit.com/submit?title=%s&url=%s'
# TELEGRAM_ENDPOINT = 'https://t.me/share/url?text=%s&url=%s'
# WHATSAPP_ENDPOINT = 'https://api.whatsapp.com/send?text=%s'
