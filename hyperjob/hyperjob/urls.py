"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from resume.views import MainMenuView, ResumeListView, SignupView, MyLoginView, NewResumeView, HomeView
from vacancy.views import VacancyListView, NewVacancyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainMenuView.as_view()),
    re_path('vacancies/?', VacancyListView.as_view()),
    re_path('resumes/?', ResumeListView.as_view()),
    re_path('login/?', MyLoginView.as_view()),
    re_path('signup/?', SignupView.as_view()),
    re_path('vacancy/new/?', NewVacancyView.as_view()),
    re_path('resume/new/?', NewResumeView.as_view()),
    re_path('home/?', HomeView.as_view()),
]
