"""courses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from coursesapi import views

# router = routers.DefaultRouter()
# router.register(r'courses', views.CoursesViewSet)


urlpatterns = [
    path('courses/', views.CoursesListView.as_view()),
    path('courses/<int:id>', views.CoursesView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
