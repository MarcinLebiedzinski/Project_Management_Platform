from django import forms
from pmplatform_app.models import Project, Task, UserTask, Report, UserDetails
from django.contrib.auth.models import User


class ProjectAddForm(forms.Form):
    name = forms.CharField(label='Project name', max_length=64)
    description = forms.CharField(label='Project description', widget=forms.Textarea)
    predicted_finish_date = forms.DateField(widget=forms.SelectDateWidget)
    manager = forms.ModelChoiceField(queryset=User.objects.all().order_by('username'), widget=forms.Select)


class TaskAddForm(forms.Form):
    name = forms.CharField(label='Task name', max_length=64)
    description = forms.CharField(label='Project description', widget=forms.Textarea)
    predicted_finish_date = forms.DateField(widget=forms.SelectDateWidget)


APROVING_CHOICES = (
        (1, "yes"),
        (2, "no"),
    )


class AprovingForm(forms.Form):
    choice = forms.ChoiceField(choices=APROVING_CHOICES, label="Are You sure?")
