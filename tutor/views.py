from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
# from rest_framework import generics
from tutor.models import Tutor, Roadmap, Section, SubSection
from tutor.serializer import RoadmapSerializer, SectionSerializer, SubSectionSerializer, TutorSerializer
from rest_framework.authtoken.models import Token


# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(token)


# tutor/roadmap/section/subsection/
# sjhdbfjshdakbf

class TutorReg(ListCreateAPIView):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

class TutorLogin(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            tutor = Tutor.objects.get(email=email, password=password)
            return Response({"message": "Tutor logged in successfully"})
        except:
            return Response({"message": "Invalid credentials"})

class SectionGen(ListCreateAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class SectionGenDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    

class RoadmapGen(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    serializer_class = RoadmapSerializer
    queryset = Roadmap.objects.all()
    

class RoadmapGenDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = RoadmapSerializer
    queryset = Roadmap.objects.all()
    
class SubSectionGen(ListCreateAPIView):
    serializer_class = SubSectionSerializer
    queryset = SubSection.objects.all()

class SubSectionGenDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SubSectionSerializer
    queryset = SubSection.objects.all()






    
    









    # def get_serializer_context(self):
    #     return {'request': self.request}

    # def get_queryset(self):
    #     return Section.objects.all()

    # def get_serializer_class(self):
    #     return SectionSerializer

# class SectionGen(APIView):
#     def get(self, request):
#         sections = Section.objects.all()
#         serializer = SectionSerializer(sections, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SectionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


    # def get(self, request):
    #     roadmaps = Roadmap.objects.all()
    #     serializer = RoadmapSerializer(roadmaps, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = RoadmapSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)


    # def get(self, request):
    #     subsections = SubSection.objects.all()
    #     serializer = SubSectionSerializer(subsections, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = SubSectionSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
# class SubSectionGen(APIView):
#     def get(self, request):
#         subsections = SubSection.objects.all()
#         serializer = SubSectionSerializer(subsections, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SubSectionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# @api_view(['GET', 'POST'])
# def section(request):
#     if request.method == 'GET':
#         sections = Section.objects.all()
#         serializer = SectionSerializer(sections, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SectionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'POST'])
# def subsection(request):
#     if request.method == 'GET':
#         subsections = SubSection.objects.all()
#         serializer = SubSectionSerializer(subsections, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SubSectionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'POST'])
# def roadmap(request):
#     if request.method == 'GET':
#         roadmaps = Roadmap.objects.all()
#         serializer = RoadmapSerializer(roadmaps, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = RoadmapSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)



# @api_view(['GET'])
# def roadmap_available(request):
#     roadmaps = Roadmap.objects.all()
#     sec = Section.objects.all()
#     section = list(Section.objects.all().values())
#     subsection = list(SubSection.objects.all().values())

    # serializer = RoadmapSerializer(roadmaps, many=True)
    # return Response(serializer.data)


    # b =  SectionSerializer(f, many=True)
    # b.subsection = subsection
    
    # serializer.sections.subsections = subsection
    
    # roadmap = Tutor.objects.earliest('user_id') #Complex data
    # roadmap_pyv = list(roadmap.user_id()) #Python DS
    # tutor = list(Tutor.objects.all().values())
    # roadmaps = list(Roadmap.objects.all().values()) 
    # subsection = list(SubSection.objects.all().values())
    # return JsonResponse({"tutor": tutor, "roadmaps": roadmaps, "section":section, "subsection": subsection}, safe=False)

# @api_view(['POST'])
# def roadmap_create(request):
#     serializer = RoadmapSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     else:
#         return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def section_create(request):
#     serializer = SectionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     else:
#         return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def subsection_create(request):
#     serializer = SubSectionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     else:
#         return Response(serializer.errors, status=400)
