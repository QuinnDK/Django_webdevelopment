from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about.html/', views.about),
    path('project.html/', views.project),
    path('services.html/', views.services),
    path('contact.html/', views.contact),
    path('components.html/', views.components),
]
