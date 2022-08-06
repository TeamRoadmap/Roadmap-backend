from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token

# from . import views
from pprint import pprint
from tutor.views import RoadmapGen, SectionGen, SubSectionGen, SectionGenDetail, SubSectionGenDetail, RoadmapGenDetail, TutorReg, TutorLogin # roadmap_create, section_create, subsection_create #, section_update, subsection_update, section_delete, subsection_delete, roadmap_delete

# router = SimpleRouter()
# router.register(r'roadmap_create', RoadmapGen.as_view())
# # router.register('section_create', SectionGen.as_view())
# # router.register('subsection_create', SubSectionGen.as_view())

# pprint(router.urls)


urlpatterns = [
    # path('tokenlogin/', views.obtain_auth_token),
    path('roadmap_create/', RoadmapGen.as_view()),
    path('reg/', TutorReg.as_view()),
    path('login/', TutorLogin.as_view()),
    path('roadmap_create/<int:pk>', RoadmapGenDetail.as_view()),
    path('section_create/', SectionGen.as_view()),
    path('section_create/<int:pk>/', SectionGenDetail.as_view()),
    path('subsection_create/', SubSectionGen.as_view()),
    path('subsection_create/<int:pk>/', SubSectionGenDetail.as_view()),
    path('auth/login/', obtain_auth_token),
    # path('list/', roadmap),
    # path('list1/', section),
    # path('list2/', subsection)
] 