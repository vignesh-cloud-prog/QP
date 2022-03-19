from django.shortcuts import render, HttpResponse, redirect
from .models import Question_paper
from django.http import request, HttpRequest, response, Http404
from django.contrib import messages
from django.core.mail import send_mail
from django.core import serializers
from profiles.models import Profile
from django.contrib.auth.models import User
# Create your views here.

# this function returns distinct values for different college types for json responce


def filter_first_option(request):
    college = Question_paper.objects.order_by(
        'education_type').distinct('education_type')
    qs_json = serializers.serialize('json', college)
    return HttpResponse(qs_json, content_type='application/json')


def colleges(request):
    """
    Displays all the college type of question papers available :model:`question_papers.Question_paper`.

    **Context**

    ``mymodel``
        An instance of :model:`question_papers.Question_paper`.

    **Template:**

    :template:`question_papers/allpapers.html`
    """
    allqp = Question_paper.objects.distinct('education_type')
    context = {'allqp': allqp, 'Select': 'Select Your Current Education : '}
    return render(request, 'question_papers/allpapers.html', context)

# this function returns distinct values for different universities and boards in college types


def college(request, college):
    """
    Display distinct values for different universities and boards in college types.

    **Context**

    ``mymodel``
        The instances of :model:`question_papers.Question_paper`.

    **Template:**

    :template:`question_papers/universities.html`
    """
    if college.startswith("json"):
        college = college.split("-")[1]
        college = Question_paper.objects.filter(
            education_type=college).order_by('education_type').distinct('education_type')
        if college.exists():
            qs_json = serializers.serialize('json', college)
            return HttpResponse(qs_json, content_type='application/json')
        # TODO : Exception to be handled
    college = Question_paper.objects.filter(
        education_type=college).order_by('governing_body').distinct('governing_body')
    if college.exists():
        print(college)
        college = {'college': college}
        return render(request, 'question_papers/universities.html', college)
    else:
        raise Http404("Page not found")


def university(request, college, university):
    """
    Display distinct values for different cousres in an universities.

    **Context**

    ``mymodel``
        The instances of :model:`question_papers.Question_paper`.

    **Template:**

    :template:`question_papers/courses.html`
    """
    if college.startswith("json"):
        college = college.split("-")[1]
        university = Question_paper.objects.filter(
            governing_body=university, education_type=college).order_by('course_name').distinct('course_name')
        qs_json = serializers.serialize('json', university)
        return HttpResponse(qs_json, content_type='application/json')
    university = Question_paper.objects.filter(
        governing_body=university, education_type=college).order_by('course_name').distinct('course_name')
    if university.exists():
        university = {'university': university}
        return render(request, 'question_papers/courses.html', university)
    else:
        raise Http404("Page not found")


def course(request, college, university, course):
    """
    Display distinct values for different semisters or years in an course.

    **Context**

    ``mymodel``
        The instances of :model:`question_papers.Question_paper`.

    **Template:**

    :template:`question_papers/classes.html`
    """
    if college.startswith("json"):
        college = college.split("-")[1]
        course = Question_paper.objects.filter(education_type=college,
            course_name=course, governing_body=university).order_by('period').distinct('period')
        qs_json = serializers.serialize('json', course)
        return HttpResponse(qs_json, content_type='application/json')
    course = Question_paper.objects.filter(education_type=college,
        course_name=course, governing_body=university).order_by('period').distinct('period')
    if course.exists():
        course = {'course': course}
        return render(request, 'question_papers/classes.html', course)
    else:
        raise Http404("Page not found")


def year(request, college, university, course, year):
    """
    Display distinct values for distinct different subjects in a semisters.

    **Context**

    ``mymodel``
        The instances of :model:`question_papers.Question_paper`.

    **Template:**

    :template:`question_papers/subjects.html`
    """
    if college.startswith("json"):
        college = college.split("-")[1]
        year = Question_paper.objects.filter(education_type=college,
            course_name=course, governing_body=university,period=year).order_by('subject_name').distinct('subject_name')
        qs_json = serializers.serialize('json', year)
        return HttpResponse(qs_json, content_type='application/json')
    year = Question_paper.objects.filter(education_type=college,
        course_name=course, governing_body=university,period=year).order_by('subject_name').distinct('subject_name')
    if year.exists():
        year = {'year': year}
        return render(request, 'question_papers/subjects.html', year)
    else:
        raise Http404("Page not found")

# this function returns distinct values for different distinct avilable years of papers of a particular subject


def question_papers(request, college, university, course, year, subject):
    """
    Display distinct values for different distinct avilable years of papers of a particular subject.

    **Context**

    ``mymodel``
        The instances of :model:`question_papers.Question_paper`.

    **Template:**

    :template:`question_papers/papers.html`
    """
    papers = Question_paper.objects.filter(
        education_type=college,
        course_name=course, governing_body=university,period=year,subject_name=subject)
    if papers.exists():
        papers = {'paper': papers}
        return render(request, 'question_papers/papers.html', papers)
    else:
        raise Http404("Page not found")

# this function returns filtered elements to a html page


def filters(request):
    """
    Function to filter the question papers.

    **Context**

    ``mymodel``
        The instances of :model:`question_papers.Question_paper`.

    **Template:**

    :template:`question_papers/filter.html`
    """
    college = request.POST.get('college')
    university = request.POST.get('university')
    course = request.POST.get('course')
    year = request.POST.get('year')
    subject = request.POST.get('subject')
    filter_obj = Question_paper.objects.filter(education_type=college).filter(period=year).filter(
        course_name=course).filter(subject_name=subject).filter(governing_body=university)
    filter_obj = {'context': filter_obj}
    return render(request, 'question_papers/filter.html', filter_obj)


def search(request):
    """
    Display all the related papers related to users search.

    **Context**

    ``mymodel``
        The instances of :model:`question_papers.Question_paper`.

    **Template:**

    :template:`question_papers/search.html`
    """
    query = request.GET['query']
    query = query.lower()
    query = query.replace(" ", "-")
    result = Question_paper.objects.filter(complete_ref__icontains=query)
    result = {'results': result}
    return render(request, 'question_papers/search.html', result)


def about(request):
    """
    Display the information related to website and developer.

    **Context**

    **Template:**

    :template:`question_papers/about.html`
    """
    return render(request, 'question_papers/about.html')

def privacy(request):
    """
    Display the information related to website and developer.
    **Context**
    **Template:**
    :template:`qp/privacy-policy.html`
    """
    return render(request, 'qp/privacy-policy.html')
def terms(request):
    """
    Display the information related to website and developer.
    **Context**
    **Template:**
    :template:`qp/terms-and-conditions.html`
    """
    return render(request, 'qp/terms-and-conditions.html')

def error_404(request, exception):
    """
    Display 404 page if user requested page doesn't exist.

    **Context**

    **Template:**

    :template:`404.html`
    """
    data = {}
    print(exception)
    return render(request, '404.html', data)

# TWITTER_ENDPOINT = 'https://twitter.com/intent/tweet?text=%s'
# FACEBOOK_ENDPOINT = 'https://www.facebook.com/sharer/sharer.php?u=%s'
# GPLUS_ENDPOINT = 'https://plus.google.com/share?url=%s'
# MAIL_ENDPOINT = 'mailto:?subject=%s&body=%s'
# LINKEDIN_ENDPOINT = 'https://www.linkedin.com/shareArticle?mini=true&title=%s&url=%s'
# REDDIT_ENDPOINT = 'https://www.reddit.com/submit?title=%s&url=%s'
# TELEGRAM_ENDPOINT = 'https://t.me/share/url?text=%s&url=%s'
# WHATSAPP_ENDPOINT = 'https://api.whatsapp.com/send?text=%s'
