"""pmplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from pmplatform_app.views import Submit, Main, UserDetails, Contact, About, ProjectCreate, InvalidData
from pmplatform_app.views import ProjectsList, ProjectDetails


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pmplatform/submit/', Submit.as_view()),
    path('pmplatform/main/', Main.as_view(), name='main'),
    path('pmplatform/contact/', Contact.as_view(), name='contact'),
    path('pmplatform/about/', About.as_view(), name='about'),
    path('pmplatform/userdetails/', UserDetails.as_view(), name='userdetails'),
    path('pmplatform/projectcreate/', ProjectCreate.as_view(), name='project_create'),
    path('pmplatform/invaliddata/', InvalidData.as_view(), name='invalid_data'),
    path('pmplatform/projectslist/', ProjectsList.as_view(), name='projects_list'),
    path('pmplatform/projectdetails/<int:project_id>/', ProjectDetails.as_view(), name='project_details')
]
