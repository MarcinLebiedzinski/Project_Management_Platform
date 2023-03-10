from django.shortcuts import render, redirect
from django.views import View

from django.http import HttpResponse, HttpResponseRedirect

from .models import Project, Task, UserTask, Report
from django.contrib.auth.models import Group, Permission, User

from pmplatform_app.forms import ProjectAddForm


# Create your views here.
class Submit(View):
    def get(self, request):
        ctx = {}
        return render(request, 'submit.html', ctx)


class Main(View):
    def get(self, request):
        return render(request, 'main.html')


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class InvalidData(View):
    def get(self, request):
        return render(request, 'invaliddata.html')


class UserDetails(View):
    def get(self, request):
        users = User.objects.all()
        ctx = {'team': users}
        return render(request, 'userdetails.html', ctx)


class ProjectCreate(View):
    def get(self, request):
        form = ProjectAddForm()
        ctx = {'form': form}
        return render(request, 'projectcreate.html', ctx)

    def post(self, request):
        form = ProjectAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            predicted_finish_date = form.cleaned_data['predicted_finish_date']
            manager = form.cleaned_data['manager']
            Project.objects.create(name=name,
                                   description=description,
                                   predicted_finish_date=predicted_finish_date,
                                   manager=manager)
            return redirect('http://127.0.0.1:8000/pmplatform/projectslist/')
        else:
            HttpResponseRedirect('http://127.0.0.1:8000/pmplatform/invaliddata/')


class ProjectsList(View):
    def get(self, request):
        projects = Project.objects.all()
        ctx = {'projects': projects}
        return render(request, 'projectslist.html', ctx)
