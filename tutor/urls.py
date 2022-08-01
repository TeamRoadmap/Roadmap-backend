from django.contrib import admin
from django.urls import path
from tutor.views import RoadmapGen, SectionGen, SubSectionGen# roadmap_create, section_create, subsection_create #, section_update, subsection_update, section_delete, subsection_delete, roadmap_delete

urlpatterns = [
    path('roadmap_create/', RoadmapGen.as_view()),
    path('section_create/', SectionGen.as_view()),
    path('subsection_create/', SubSectionGen.as_view()),
    # path('list/', roadmap),
    # path('list1/', section),
    # path('list2/', subsection)
] 