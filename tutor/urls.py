from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
# from . import views
from pprint import pprint
from tutor.views import RoadmapGen, SectionGen, SubSectionGen, SectionGenDetail, SubSectionGenDetail, RoadmapGenDetail, Signup #, Login #AuthRegistrationView, AuthLoginView,  #, Login #, TutorReg #TutorLogin # roadmap_create, section_create, subsection_create #, section_update, subsection_update, section_delete, subsection_delete, roadmap_delete

# router = SimpleRouter()
# router.register(r'roadmap_create', RoadmapGen.as_view())
# # router.register('section_create', SectionGen.as_view())
# # router.register('subsection_create', SubSectionGen.as_view())

# pprint(router.urls)

# 
urlpatterns = [
    # path('tokenlogin/', views.obtain_auth_token),
    path('roadmap_create/', RoadmapGen.as_view()),
    path('reg/', Signup.as_view()),
    # path('login/', Login.as_view()),
    path('roadmap_create/<int:pk>', RoadmapGenDetail.as_view()),
    path('section_create/', SectionGen.as_view()),
    path('section_create/<int:pk>/', SectionGenDetail.as_view()),
    path('subsection_create/', SubSectionGen.as_view()),
    path('subsection_create/<int:pk>/', SubSectionGenDetail.as_view()),
    path('login/', obtain_auth_token),


    # path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('register', AuthRegistrationView.as_view(), name='register'),
    # path('login', AuthLoginView.as_view(), name='login'),
    # path('users', UserListView.as_view(), name='users')
    # path('list/', roadmap),
    # path('list1/', section),
    # path('list2/', subsection)
] 