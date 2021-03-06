from django.shortcuts import render, HttpResponse, redirect
from .models import Question_paper
from django.http import request, HttpRequest
from django.contrib import messages
from django.core.mail import send_mail
from django.core import serializers
from profiles.models import Profile
from django.contrib.auth.models import User
# Create your views here.

# this function returns distinct values for different college types for json responce


def filter_first_option(request):
    college = Question_paper.objects.order_by('college').distinct('college')
    qs_json = serializers.serialize('json', college)
    return HttpResponse(qs_json, content_type='application/json')

# this function returns distinct values for different college types


def colleges(request):
    allqp = Question_paper.objects.order_by('college').distinct('college')
    context = {'allqp': allqp, 'Select': 'Select Your Current Education : '}
    return render(request, 'question_papers/colleges.html', context)

# this function returns distinct values for different universities and boards in college types


def college(request, college):
    if college.startswith("json"):
        college = college.split("-")[1]
        college = Question_paper.objects.filter(
            college=college).order_by('university').distinct('university')
        qs_json = serializers.serialize('json', college)
        return HttpResponse(qs_json, content_type='application/json')

    college = Question_paper.objects.filter(
        college=college).order_by('university').distinct('university')
    college = {'college': college}
    return render(request, 'question_papers/universities.html', college)

# this function returns distinct values for different cousres in an universities


def university(request, college, university):
    if college.startswith("json"):
        college = college.split("-")[1]
        university = Question_paper.objects.filter(
            university=university, college=college).order_by('course').distinct('course')
        qs_json = serializers.serialize('json', university)
        return HttpResponse(qs_json, content_type='application/json')
    university = Question_paper.objects.filter(
        university=university, college=college).order_by('course').distinct('course')
    university = {'university': university}
    return render(request, 'question_papers/courses.html', university)

# this function returns distinct values for different semisters or years in an course


def course(request, college, university, course):
    if college.startswith("json"):
        college = college.split("-")[1]
        course = Question_paper.objects.filter(
            course=course, university=university).order_by('year').distinct('year')
        qs_json = serializers.serialize('json', course)
        return HttpResponse(qs_json, content_type='application/json')
    course = Question_paper.objects.filter(
        course=course, university=university).order_by('year').distinct('year')
    course = {'course': course}
    return render(request, 'question_papers/classes.html', course)

# this function returns distinct values for distinct different subjects in a semisters


def year(request, college, university, course, year):
    if college.startswith("json"):
        college = college.split("-")[1]
        year = Question_paper.objects.filter(
            course=course, university=university).order_by('subject').distinct('subject')
        qs_json = serializers.serialize('json', year)
        return HttpResponse(qs_json, content_type='application/json')
    year = Question_paper.objects.filter(
        course=course, university=university).order_by('subject').distinct('subject')
    year = {'year': year}
    return render(request, 'question_papers/subjects.html', year)

# this function returns distinct values for different distinct avilable years of papers of a particular subject


def question_papers(request, college, university, course, year, subject):
    papers = Question_paper.objects.filter(
        subject=subject, university=university)
    papers = {'paper': papers}
    return render(request, 'question_papers/papers.html', papers)



# this function returns filtered elements to a html page


def filters(request):
    college = request.POST.get('college')
    university = request.POST.get('university')
    course = request.POST.get('course')
    year = request.POST.get('year')
    subject = request.POST.get('subject')
    filter_obj = Question_paper.objects.filter(college=college).filter(year=year).filter(
        course=course).filter(subject=subject).filter(university=university)
    filter_obj = {'context': filter_obj}
    return render(request, 'question_papers/filter.html', filter_obj)






def search(request):
    query = request.GET['query']
    query = query.lower()
    query = query.replace(" ", "_")
    result = Question_paper.objects.filter(slug__icontains=query)
    result = {'results': result}
    return render(request, 'question_papers/search.html', result)




# TWITTER_ENDPOINT = 'https://twitter.com/intent/tweet?text=%s'
# FACEBOOK_ENDPOINT = 'https://www.facebook.com/sharer/sharer.php?u=%s'
# GPLUS_ENDPOINT = 'https://plus.google.com/share?url=%s'
# MAIL_ENDPOINT = 'mailto:?subject=%s&body=%s'
# LINKEDIN_ENDPOINT = 'https://www.linkedin.com/shareArticle?mini=true&title=%s&url=%s'
# REDDIT_ENDPOINT = 'https://www.reddit.com/submit?title=%s&url=%s'
# TELEGRAM_ENDPOINT = 'https://t.me/share/url?text=%s&url=%s'
# WHATSAPP_ENDPOINT = 'https://api.whatsapp.com/send?text=%s'
