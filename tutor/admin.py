from django.contrib import admin
from .models import Roadmap, Section, SubSection, AuthUser

admin.site.register(AuthUser)
admin.site.register(Roadmap)
admin.site.register(Section)
admin.site.register(SubSection)
