from django.contrib import admin
from django.urls import path
from tutor.views import roadmap_available, roadmap_create, section_create, subsection_create #, section_update, subsection_update, section_delete, subsection_delete, roadmap_delete

urlpatterns = [
    path('roadmap_create', roadmap_create),
    path('section_create/', section_create),
    path('subsection_create/', subsection_create),
    path('list/', roadmap_available)
] 