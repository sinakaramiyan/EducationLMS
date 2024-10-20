from django.contrib import admin
from .models import IndividualCourseLessons, IndividualCourseLessonsComplete

admin.site.register(IndividualCourseLessons)

admin.site.register(IndividualCourseLessonsComplete)