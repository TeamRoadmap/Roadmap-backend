from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tutor.models import Tutor, Roadmap, Section, SubSection
from tutor.serializer import RoadmapSerializer, SectionSerializer
# tutor/roadmap/section/subsection/


@api_view(['GET'])
def roadmap_available(request):
    roadmaps = Roadmap.objects.all()
    sec = Section.objects.all()
    section = list(Section.objects.all().values())
    subsection = list(SubSection.objects.all().values())

    f = []
    for i in sec : 
        f.append({
            "id" : i.id,
            "section_title" : i.section_title,
            "section_description" : i.section_description,
            # "roadmap" : i.roadmap.id,
            "subsections" : subsection
        })

    d = []
    for i in roadmaps : 
        d.append({
            "id" : i.id,
            "course_name" : i.course_name,
            "course_title" : i.course_title,
            "course_description" : i.course_description,
            "tutor" : i.tutor.id,
            "sections" : f
            #     "id" : sec.id,
            #     "section_title" : sec.section_title,
            #     "section_description" : sec.section_description,
            #     "roadmap" : sec.roadmap.id,
            #     "subsections" : subsection
            # 

        })
    serializer = RoadmapSerializer(d, many=True)
    serializer.sections = section
    return Response(serializer.data)


    # b =  SectionSerializer(f, many=True)
    # b.subsection = subsection
    
    # serializer.sections.subsections = subsection
    
    # roadmap = Tutor.objects.earliest('user_id') #Complex data
    # roadmap_pyv = list(roadmap.user_id()) #Python DS
    # tutor = list(Tutor.objects.all().values())
    # roadmaps = list(Roadmap.objects.all().values()) 
    # subsection = list(SubSection.objects.all().values())
    # return JsonResponse({"tutor": tutor, "roadmaps": roadmaps, "section":section, "subsection": subsection}, safe=False)

@api_view(['POST'])
def roadmap_create(request):
    serializer = RoadmapSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def section_create(request):
    serializer = SectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def subsection_create(request):
    serializer = SubSectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
        