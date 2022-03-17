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
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('profiles.urls')),
    path('contact/', include('contacts.urls')),
    path('provider/', include('provides.urls')),
    path('push/', include('provides_controller.urls')),
    path('', include('question_papers.urls')),
]

admin.site.site_header="QP Administration"

