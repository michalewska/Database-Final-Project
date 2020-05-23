from django.contrib import admin
from .models import Meeting, Course, Project, Activity

# Register your models here.
admin.site.register(Course)
admin.site.register(Meeting)
admin.site.register(Project)
admin.site.register(Activity)
