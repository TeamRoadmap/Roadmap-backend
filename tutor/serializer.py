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

class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        user_obj = None
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user_obj = AuthUser.objects.filter(email=email).first()
            if not user_obj:
                raise serializers.ValidationError("This email is not registered")
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect credentials")
        return data
    
    def create(self, validated_data):
        user = AuthUser.objects.get(email=validated_data['email'])
        refresh = RefreshToken.for_user(user)
        return {
            'user': user,
            'token': str(refresh.access_token)
        }

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





