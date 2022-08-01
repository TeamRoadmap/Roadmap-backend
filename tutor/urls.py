from django.contrib import admin
from django.urls import path
from tutor.views import roadmap, section, subsection# roadmap_create, section_create, subsection_create #, section_update, subsection_update, section_delete, subsection_delete, roadmap_delete

urlpatterns = [
    path('roadmap_create/', roadmap),
    path('section_create/', section),
    path('subsection_create/', subsection),
    # path('list/', roadmap),
    # path('list1/', section),
    # path('list2/', subsection)
] 