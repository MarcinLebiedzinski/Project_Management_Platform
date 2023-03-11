from django.shortcuts import render, redirect
from django.views import View

from django.http import HttpResponse, HttpResponseRedirect

from .models import Project, Task, UserTask, Report
from django.contrib.auth.models import Group, Permission, User

from pmplatform_app.forms import ProjectAddForm, TaskAddForm, AprovingForm, APROVING_CHOICES


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


class UsersList(View):
    def get(self, request):
        users = User.objects.all()
        ctx = {'team': users}
        return render(request, 'userslist.html', ctx)


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


class ProjectDetails(View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        manager = User.objects.get(id=project.manager_id)
        ctx = {'project': project, 'manager': manager}
        return render(request, 'projectdetails.html', ctx)


class TasksList(View):
    def get(self, request, project_id):
        tasks = Task.objects.filter(project_id=project_id)
        project = Project.objects.get(id=project_id)
        ctx = {'tasks': tasks, 'project': project}
        return render(request, 'taskslist.html', ctx)


class TaskCreate(View):
    def get(self, request, project_id):
        form = TaskAddForm()
        ctx = {'form': form}
        return render(request, 'taskcreate.html', ctx)

    def post(self, request, project_id):
        form = TaskAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            predicted_finish_date = form.cleaned_data['predicted_finish_date']
            Task.objects.create(name=name,
                                description=description,
                                predicted_finish_date=predicted_finish_date,
                                project_id=project_id)
            return redirect('tasks_list', project_id=project_id)
        else:
            HttpResponseRedirect('invalid_data')


class TaskDelete(View):
    def get(self, request, project_id, task_id):
        form = AprovingForm(request.POST)
        ctx = {'form': form}
        return render(request, 'deletetemplate.html', ctx)

    def post(self, request, project_id, task_id):
        form = AprovingForm(request.POST)
        if form.is_valid():
            choice_dict = dict(APROVING_CHOICES)
            choice = choice_dict[int(form.cleaned_data['choice'])]
            if choice == 'yes':
                t = Task.objects.get(id=task_id)
                t.delete()
                return redirect('tasks_list', project_id=project_id)
            else:
                return redirect('tasks_list', project_id=project_id)
        else:
            HttpResponseRedirect('invalid_data')


class TaskDetails(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        users_id = UserTask.objects.filter(task_id=task_id)
        users_list = []
        for user in users_id:
            users_list.append(User.objects.get(id=user))
        ctx = {'task': task, 'users_list': users_list}
        return render(request, 'taskdetails.html', ctx)


class ProjectDelete(View):
    def get(self, request, project_id):
        form = AprovingForm(request.POST)
        ctx = {'form': form}
        return render(request, 'deletetemplate.html', ctx)

    def post(self, request, project_id):
        form = AprovingForm(request.POST)
        if form.is_valid():
            choice_dict = dict(APROVING_CHOICES)
            choice = choice_dict[int(form.cleaned_data['choice'])]
            if choice == 'yes':
                p = Project.objects.get(id=project_id)
                p.delete()
                return redirect('projects_list')
            else:
                return redirect('projects_list')
        else:
            HttpResponseRedirect('invalid_data')
