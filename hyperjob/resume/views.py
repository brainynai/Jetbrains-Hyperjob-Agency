from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied


class MainMenuView(View):
    def get(self, request):
        return render(request, "resume/mainMenu.html", context={})


class ResumeListView(View):
    def get(self, request):
        resumes = Resume.objects.all()
        return render(request, "resume/allresumes.html", context={'resumes':resumes})


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = 'resume/signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = "/"
    template_name = 'resume/login.html'


class NewResumeView(View):
    def get(self, request):
        return render(request, 'resume/newresume.html', context={})

    def post(self, request):
        thisUser = request.user
        if not thisUser.is_authenticated:
            raise PermissionDenied

        desc = request.POST.get('description')
        Resume.objects.create(description=desc, author=thisUser)

        return redirect('/home')


class HomeView(View):
    def get(self, request):
        thisUser = request.user
        if not thisUser.is_authenticated:
            return redirect('resume/new')
        elif thisUser.is_staff:
            return redirect('vacancy/new')
        else:
            return redirect('resume/new')
