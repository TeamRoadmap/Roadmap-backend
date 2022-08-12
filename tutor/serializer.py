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

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user_obj = AuthUser.objects.get(email=email)
                if not user_obj.check_password(password):
                    raise serializers.ValidationError("Incorrect credentials")
                data['user'] = user_obj
            except AuthUser.DoesNotExist:
                raise serializers.ValidationError("This email is not registered")
        else:
            raise serializers.ValidationError("Missing credentials")
        return data


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





