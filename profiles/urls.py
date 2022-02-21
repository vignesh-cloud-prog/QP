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
from profiles import views
from django.views.generic import RedirectView


urlpatterns = [

    path('update', views.profile_settings, name='update_profile'),
    path('', views.profile_view, name='profile'),
    path('favicon.ico/',RedirectView.as_view(url='/static/favicon.ico')),
        
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
