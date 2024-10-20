from django.contrib import admin
from .models import IndividualCourseQuiz, IndividualCourseQuizSubmit, IndividualCourseQuizPoints

admin.site.register(IndividualCourseQuiz)

admin.site.register(IndividualCourseQuizPoints)

admin.site.register(IndividualCourseQuizSubmit)