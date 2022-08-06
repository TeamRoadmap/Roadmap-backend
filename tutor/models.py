from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Tutor(models.Model):
    first_name = models.CharField(max_length=255, default='suraj')
    last_name = models.CharField(max_length=255, default='singh')
    email = models.CharField(max_length=255, default='abc@crework.com')
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Roadmap(models.Model):
    course_name = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    course_description = models.TextField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

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
    


    # image = models.ImageField(upload_to='files/subsections')




