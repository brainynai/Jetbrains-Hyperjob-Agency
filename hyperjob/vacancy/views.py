from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.core.exceptions import PermissionDenied


class VacancyListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request, "vacancy/allresumes.html", context={'resumes':vacancies})


class NewVacancyView(View):
    def get(self, request):
        return render(request, 'vacancy/newvacancy.html', context={})

    def post(self, request):
        thisUser = request.user
        if not thisUser.is_authenticated or not thisUser.is_staff:
            raise PermissionDenied

        desc = request.POST.get('description')
        Vacancy.objects.create(description=desc, author=thisUser)

        return redirect('/home/')
