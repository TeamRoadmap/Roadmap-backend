from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class AuthUser(AbstractUser):
    ADMIN = 'A'
    STUDENT = 'S'
    TUTOR = 'T'
    ROLE_CHOICES = (
        (ADMIN, 'Superuser'),
        (STUDENT, 'Student'),
        (TUTOR, 'Tutor'),
    )
    username = None
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=STUDENT)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email

class Roadmap(models.Model):
    course_name = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    course_description = models.TextField()
    # tutor = NewUser.ForeignKey(NewUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

class Section(models.Model):
    section_title = models.CharField(max_length=255)
    section_description = models.TextField()
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)

    def __str__(self):
        return self.section_title

    # image = models.ImageField(upload_to='files/sections/')

class SubSection(models.Model):
    subsection_title = models.CharField(max_length=255)
    subsection_description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsection_title

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    



# class User(AbstractUser):
#     is_tutor = models.BooleanField(default=False)


# class Tutor(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#     USERNAME_FIELD = 'email'
    


#     def __str__(self):
#         return self.first_name
    # image = models.ImageField(upload_to='files/subsections')




