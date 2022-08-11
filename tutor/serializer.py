from os import access
from rest_framework import serializers
from .models import Section, SubSection, Roadmap, AuthUser
from rest_framework_simplejwt.tokens import RefreshToken


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('first_name', 'last_name', 'email', 'password', 'role')
    
    def create(self, data):
        return AuthUser.objects.create_user(**data)

class SubSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSection
        fields = ('__all__')
    
    def create(self, data):
        return SubSection.objects.create(**data)
class SectionSerializer(serializers.ModelSerializer):
    # subsections = SubSectionSerializer(many=True, read_only=True)
    class Meta:
        model = Section
        fields = '__all__'
    
    def create(self, data):
        return Section.objects.create(**data)
class RoadmapSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    class Meta:
        model = Roadmap
        fields = '__all__'
    
    def create(self, data):
        return Roadmap.objects.create(**data)





