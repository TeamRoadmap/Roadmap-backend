from django.db import models

# tutor/roadmap/section/subsection/

class Tutor(models.Model):
    user_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_id 

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


    # image = models.ImageField(upload_to='files/subsections')




