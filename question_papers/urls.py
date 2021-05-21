"""qp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from question_papers import views

urlpatterns = [

    path('profile/update', views.profile_settings, name='update_profile'),
    path('provider/', views.provider, name='provider'),
    path('search/', views.search, name='search'),
    path('push/', views.push, name='push'),
    path('push/pushed', views.pushed, name='pushed'),
    path('contact/', views.issues, name='contact'),
    path('filter', views.filters, name='filter'),
    path('filter_first_option', views.filter_first_option, name='filter_first_option'),

    path('', views.colleges, name='home'),
        path('<str:college>/', views.college, name='college'),
        path('<str:college>/<str:university>/', views.university, name='university'),
        path('<str:college>/<str:university>/<str:course>/', views.course, name='course'),
        path('<str:college>/<str:university>/<str:course>/<str:year>/', views.year, name='year'),
        path('<str:college>/<str:university>/<str:course>/<str:year>/<str:subject>/', views.question_papers, name='question_papers'),
        
        # path('board/<str:board_type>/', views.college, name='college'),
        # path('board/<str:board_type>/<str:board_name>/', views.university, name='university'),
        # path('board/<str:board_type>/<str:board_name>/', views.course, name='course'),
        # path('board/<str:board_type>/<str:board_name>/<str:year>/', views.year, name='year'),
        # path('board/<str:board_type>/<str:board_name>/<str:year>/<str:subject>/', views.question_papers, name='question_papers'),
        
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
