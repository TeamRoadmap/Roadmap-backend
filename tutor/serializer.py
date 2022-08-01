from rest_framework import serializers
from .models import Tutor, Section, SubSection, Roadmap

class SubSectionSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        subsection_title = serializers.CharField()
        subsection_description = serializers.CharField()
        section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())

        def create(self, data):
            return SubSection.objects.create(**data)

class SectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    section_title = serializers.CharField()
    section_description = serializers.CharField()
    # roadmap = serializers.PrimaryKeyRelatedField(queryset=Roadmap.objects.all())
    # roadmap = serializers.IntegerField()
    # subsections = SubSectionSerializer(many=True)
    # roadmap = serializers.PrimaryKeyRelatedField(queryset=Roadmap.objects.all())
    subsections = SubSectionSerializer()
    
    def create(self, data):
        return Section.objects.create(**data)
        # subsections = validated_data.pop('subsections')
        # section = Section.objects.create(**validated_data)
        # for subsection_data in subsections:
        #     SubSection.objects.create(section=section, **subsection_data)
        # return section

class RoadmapSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    course_name = serializers.CharField()
    course_title = serializers.CharField()
    course_description = serializers.CharField()
    # tutor = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all()) #Problem with foreign key
    # tutor = serializers.CharField(max_length=255)
    tutor = serializers.IntegerField()
    sections = SectionSerializer(many=True, read_only=True)

    def create(self, data):
        return Roadmap.objects.create(**data)

        # sections_data = validated_data.pop('sections')
        # roadmap = Roadmap.objects.create(**validated_data)
        # for section_data in sections_data:
        #     section = Section.objects.create(roadmap=roadmap, **section_data)
        #     for subsection_data in section_data['subsections']:
        #         SubSection.objects.create(section=section, **subsection_data)
        # return roadmap




