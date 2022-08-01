from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tutor.models import Tutor, Roadmap, Section, SubSection
from tutor.serializer import RoadmapSerializer, SectionSerializer, SubSectionSerializer
# tutor/roadmap/section/subsection/


@api_view(['GET', 'POST'])
def section(request):
    if request.method == 'GET':
        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def subsection(request):
    if request.method == 'GET':
        subsections = SubSection.objects.all()
        serializer = SubSectionSerializer(subsections, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def roadmap(request):
    if request.method == 'GET':
        roadmaps = Roadmap.objects.all()
        serializer = RoadmapSerializer(roadmaps, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoadmapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



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
