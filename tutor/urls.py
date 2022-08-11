from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('roadmap_create/', views.RoadmapGen.as_view()),
    path('reg/', views.Signup.as_view()),
    path('roadmap_create/<int:pk>', views.RoadmapGenDetail.as_view()),
    path('section_create/', views.SectionGen.as_view()),
    path('section_create/<int:pk>/', views.SectionGenDetail.as_view()),
    path('subsection_create/', views.SubSectionGen.as_view()),
    path('subsection_create/<int:pk>/', views.SubSectionGenDetail.as_view()),
    path('login/', views.AuthLoginUser.as_view()),
] 
