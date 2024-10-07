"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from profiles import views
from projects import views as projek
from contact import views as contact
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('webapp.urls')),
    path('', views.profiles),
    path('resume/', views.resume),
    path('project/', projek.projects),
    path('project/<int:pk>/', projek.project_detail, name='project_detail'),
    path('contact/',contact.contact),
    path('respon/',contact.response, name="respon"),

]
