from os import access
from rest_framework import serializers
from .models import Section, SubSection, Roadmap, AuthUser #Tutor
from rest_framework_simplejwt.tokens import RefreshToken


#—————serializers.py—————

# class TutorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tutor
#         fields = ('first_name', 'last_name', 'email', 'password')
    
#     def create(self, data):
#         return Tutor.objects.create(**data)
    
# class TutorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tutor
#         fields = ('user_id', 'password')


# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuthUser
#         fields = ('first_name', 'last_name', 'email', 'password')
    
#     def create(self, data):
#         return AuthUser.objects.create(**data)

# class LoginSerializer(serializers.ModelSerializer):

#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=128, write_only=True)
#     access = serializers.CharField(read_only=True)
#     refresh = serializers.CharField(read_only=True)
#     role = serializers.CharField(read_only=True)

#     def validated_data(self, data):
#         email = data['email']
#         password = data['password']
#         user = authenticate(email=email, password=password)
#         if user is None:
#             raise serializers.ValidationError('A user with this email and password is not found.')
#         try:
#             refresh = RefreshToken.for_user(user)
#             refresh_token = str(refresh)
#             access_token = str(refresh.access_token)

#             update_last_login(None, user)

#             validation = {
#                 'email': email,
#                 'password': password,
#                 'access': access_token,
#                 'refresh': refresh_token,
#                 'role': user.role
#             }
#             return validation

#         except Exception as e:
#             raise serializers.ValidationError(str(e))


# class ListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuthUser
#         fields = ('email', 'role')
    



class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('first_name', 'last_name', 'email', 'password', 'role')
    
    def create(self, data):
        return AuthUser.objects.create(**data)

class AuthCustomTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)

    def validated(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password is not found.')
        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            return {
                'email': email,
                'password': password,
                'access': access_token,
                'refresh': refresh_token,
                'role': user.role
            }
        except Exception as e:
            raise serializers.ValidationError(str(e))

# class AuthLoginUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AuthUser
#         fields = ('email', 'password')


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
        # fields = ('course_name', 'course_title', 'course_description', 'tutor', 'sections')





